BEGIN TRANSACTION;
CREATE TABLE student (id text PRIMARY KEY, password text);
INSERT INTO "student" VALUES('s12345','abcd');
COMMIT;
