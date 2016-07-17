class User:
    def __init__(self, name):
        self.name = name
        # Default version of User
        self.version = '1.0'

    def switchToNewVersion(self, version):
        self.version = version

    def __str__(self):
        return '[Name: '+ self.name + ' Version: ' + self.version+']'
