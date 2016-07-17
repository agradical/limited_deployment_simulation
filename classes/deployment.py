from total_deployment import TotalDeployment
from limited_deployment import LimitedDeployment
from exact_deployment import ExactDeployment

class Deployment:
    def __init__(self, graph, version):
        self.graph = graph
        self.version = version

    # Deploy helper method to invoke corresponding Deployment
    # procedure based on input arguments
    def deploy(self, user, threshold=None, strict=None):

        affected_nodes = 0;

        if threshold is None:
            newversion = TotalDeployment(self.graph, self.version, user)
            affected_nodes = newversion.deploy()

        elif strict is None:
            newversion = LimitedDeployment(self.graph, self.version, user, threshold)
            affected_nodes = newversion.deploy()

        elif strict == 'strict':
            newversion = ExactDeployment(self.graph, self.version, user, threshold)
            affected_nodes = newversion.deploy()

        print 'Total Affected Nodes: '+ `affected_nodes`
