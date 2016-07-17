from usergraph import Graph
import Queue

class ExactDeployment:
    def __init__(self, graph, version, user, threshold):
        self.graph = graph
        self.root = user
        self.threshold = threshold
        self.version = version

    # BFS approach to spread the infection from a give node
    # and raise error if there's inconsistency in infection
    def deploy(self):
        queue = Queue.Queue()
        queue.put(self.root)
        visited = {}
        while not queue.empty():
            user = queue.get()
            visited[user.name] = True
            connections = self.graph.connections[user.name]
            for index in connections:
                if index not in visited:
                    queue.put(connections[index])

        if len(visited) != self.threshold:
            raise Exception('Deployment failed')
        else:
            for name in visited:
                user = self.graph.getUser(name)
                user.switchToNewVersion(self.version)

        return len(visited)
