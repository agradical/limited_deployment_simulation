from usergraph import Graph
import Queue

class TotalDeployment:
    def __init__(self, graph, version, user):
        self.graph = graph
        self.root = user
        self.version = version

    # BFS approach to spread infection from a given node
    def deploy(self):
        queue = Queue.Queue()
        queue.put(self.root)
        visited = {}
        while not queue.empty():
            user = queue.get()
            visited[user.name] = True
            user.switchToNewVersion(self.version)
            connections = self.graph.connections[user.name]
            for index in connections:
                if index not in visited:
                    queue.put(connections[index])

        return len(visited)
