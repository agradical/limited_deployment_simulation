from users import User

# Graph structure of user
class Graph:
    def __init__(self):
        # Maintains dictionary of Nodes and Edges
        self.users = {}
        self.connections = {}

    def addUser(self, user):
        if user.name in self.users:
            return None
        else:
            self.users[user.name] = user
            return True

    def getUser(self, name):
        if name in self.users:
            return self.users[name]
        else:
            return None

    # Add a new edge in the graph
    def addConnection(self, user1, user2, isBidirectional):
        if user1.name not in self.users:
            self.addUser(user1)
        if user2.name not in self.users:
            self.addUser(user2)

        if user1.name not in self.connections:
            self.connections[user1.name] = {}
        if user2.name not in self.connections:
            self.connections[user2.name] = {}

        if isBidirectional == True:
            self.connections[user1.name][user2.name] = user2
            self.connections[user2.name][user1.name] = user1

        else:
            self.connections[user1.name][user2.name] = user2

    def getAllUsers(self):
        return self.users
