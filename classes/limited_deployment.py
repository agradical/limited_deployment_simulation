from usergraph import Graph

class LimitedDeployment:
    def __init__(self, graph, version, user, threshold):
        self.graph = graph
        self.root = user
        self.threshold = threshold
        self.version = version

        # determines how close the infection number to the threshold
        # e.g. if tolearnce=1 and threshold=4 infected nodes will be
        # between 3 and 5
        self.tolerance = 1

    def deploy(self):

        visited = {}
        path = []
        stack = []
        stack.append(self.root)
        limit = int(self.threshold)

        inconsistency = 1
        min_inconsistency = 1
        min_inconsistency_node = self.root.name

        # DFS approach to minimize the inconsistencies among the Nodes
        while len(stack) != 0 and limit+self.tolerance != 0:
            user = stack.pop()
            connections = self.graph.connections[user.name]
            visited[user.name] = True
            path.append(user.name)
            for index in connections:
                if index not in visited:
                    # Add all univisted children to the stack
                    inconsistency += 1
                    stack.append(connections[index])

            limit -= 1
            inconsistency -= 1

            # check for the minimum inconsistency in the tolerance region
            # and set the min inconsistency node
            if limit == self.tolerance:
                min_inconsistency = inconsistency
                min_inconsistency_node = user.name

            if limit < self.tolerance and limit >= self.tolerance*-1:
                if inconsistency < min_inconsistency:
                    min_inconsistency = inconsistency
                    min_inconsistency_node = user.name

        # Iterate over the path till min inconsistency node
        # and deploy new version
        count = 0
        for name in path:
            count += 1;
            if name != min_inconsistency_node:
                user = self.graph.getUser(name)
                user.switchToNewVersion(self.version)
            else:
                user = self.graph.getUser(name)
                user.switchToNewVersion(self.version)
                break

        return count
