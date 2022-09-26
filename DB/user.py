import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()

    def getUserName(self):
        return self.username

    def setUserName(self, userName: str):
        self.userName = userName

    def getPassword(self):
        return self.password

    # set encodePassword with encoding the password
    def setPassword(self, password: str):
        self.password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()

