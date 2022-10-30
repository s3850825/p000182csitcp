class User():
    def setStudentInfo(self, username, database):
        self.username = username
        self.walletPassword = database.getStudentWalletPassword(self.username)
        self.publicKey = database.getStudentPublicKey(self.username)
        self.privateKey = database.getStudentPrivateKey(self.username)
        self.privateKeyPath = ''
    
    def getStudentName(self):
        return self.username

    def getWalletPassword(self):
        return self.walletPassword

    def getPublicKey(self):
        return self.publicKey

    def getPrivateKey(self):
        return self.privateKey

    def getPrivateKeyPath(self):
        return self.privateKeyPath

