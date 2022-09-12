import sqlite3

class bcDB:
    def __init__(self, kwargs):
        self._filename = kwargs.get('filename')

    def __connect__(self):
        """
        connect to database
        :return: connection
        """
        print('connect')
        self._db = sqlite3.connect(self._filename)
        return self._db

    def get_cursor(self):
        """
        generate the cursor
        :return: cursor
        """
        self._cursor = self._db.cursor()
        return self._cursor

    def set_table(self, tablename):
        """
        :param tablename:  string containing table name
        :return: nothing
        """
        self._table = tablename

    def sql_execute(self, sql, *params):
        """
        non-select queries
        :param sql: string containing SQL
        :param params: list containing parameters
        :return: nothing
        """
        self._db.execute(sql, params)
        self._db.commit()

    def sql_execute_no_commit(self, sql, *params):
        """
        non-select queries without commit
        :param sql: string containing SQL
        :param params: list containing parameters
        :return: nothing
        """
        self._db.execute(sql, params)

    def sql_query(self, sql, *params):
        """
        generator for queries
        :param sql: string containing SQL
        :param params: list containing parameters
        :return: generator with one row per iteration
        """
        res = self._db.execute(sql, params)
        for row in res:
            yield row

    def sql_query_row(self, sql, *params):
        """
        query for single row
        :param sql: string containing SQL
        :param params: list containing parameters
        :return: single row as a Row factory
        """
        res = self._db.execute(sql, params)
        return res.fetchone()

    def sql_query_value(self, sql, *params):
        """
        query for single value
        :param sql: string containing SQL
        :param params: list containing parameters
        :return: single value
        """
        c = self._db.execute(sql, params)
        return c.fetchone()[0]

    def commit(self):
        self._db.commit()

    def insert_no_commit(self, rec):
        """
            insert_no_commit(rec)
            insert a single record into the table
                rec is a dict with key/value pairs corresponding to table schema
            omit id column to let SQLite generate it
        """
        klist = sorted(rec.keys())
        values = [rec[v] for v in klist]  # a list of values ordered by key
        q = 'INSERT INTO {} ({}) VALUES ({})'.format(
            self._table,
            ', '.join(klist),
            ', '.join('?' * len(values))
        )
        c = self._db.execute(q, values)
        return c.lastrowid

    def insert(self, rec):
        lastrowid = self.insert_no_commit(rec)
        self._db.commit()
        return lastrowid

    def update_no_commit(self, recid, rec):
        """
            update_no_commit(id, rec)
            update a row in the table
                id is the value of the id column for the row to be updated
                rec is a dict with key/value pairs corresponding to table schema
        """
        klist = sorted(rec.keys())
        values = [rec[v] for v in klist]  # a list of values ordered by key

        for i, k in enumerate(klist):  # don't udpate id
            if k == 'id':
                del klist[i]
                del values[i]

        q = 'UPDATE {} SET {} WHERE id = ?'.format(
            self._table,
            ',  '.join(map(lambda s: '{} = ?'.format(s), klist))
        )
        self._db.execute(q, values + [recid])

    def update(self, recid, rec):
        self.update_no_commit(recid, rec)
        self._db.commit()

    def delete_no_commit(self, recid):
        """
            delete_no_commit(recid)
            delete a row from the table, by recid
        """
        query = f'DELETE FROM {self._table} WHERE id = ?'
        self._db.execute(query, [recid])

    def delete(self, recid):
        self.delete_no_commit(recid)
        self._db.commit()

