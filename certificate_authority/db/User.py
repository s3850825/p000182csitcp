import hashlib

class User:
    def __init__(self, username: str, password: str):
        self._name = username
        self._password = self.encodeByHash(password)

    def encodeByHash(self, args):
        return hashlib.md5(args)

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def set_name(self, username: str):
        self._name = username

    def set_password(self, password: str):
        self._password = self.encodeByHash(password)