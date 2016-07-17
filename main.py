import sys
sys.path.append('classes')

from usergraph import Graph
from users import User
from deployment import Deployment
import networkx as nx
import matplotlib.pyplot as plt


def printAllUsers(graph):
    users = graph.getAllUsers()
    for user in users:
        print users[user]

# provide visualization for the graph
def plotGraph(graph):
    G = nx.Graph()
    node_color = []
    count = 0

    for user_name in graph.users:
        user = graph.getUser(user_name)

        # changing node color based on the version
        if user.version == '1.0':
            node_color.append('b')
        else:
            node_color.append('r')

        count += 1
        G.add_node(user_name)

    for key, val_dict in graph.connections.iteritems():
        for val_key in val_dict:
            G.add_edge(key, val_key)

    nx.draw(G, with_labels=True, node_size=250, node_color=node_color)
    plt.show()
    plt.savefig("graph.png")

def main(argv):
    file = argv[1];
    graph = Graph();

    # read input file of teacher and student relation and create graph network
    with open(file) as f:
        for line in f:
             line = line.strip().split(',')
             user1 = User(line[0])
             user2 = User(line[1])
             graph.addConnection(user1, user2, True)

    version = '2.0'

    newversion = Deployment(graph, version)

    print "----Initial state:----"
    printAllUsers(graph)

    # Ask admin to select the node to start the deployment process
    node = raw_input('Select node to deploy: ')
    user = graph.getUser(node)
    threshold = None
    strict = None

    isthreshold = raw_input('Do you want to limit the infection[y/n]: ')
    if isthreshold == 'y':
        threshold = int(raw_input('Enter the limit: '))
        isstrict = raw_input('Is this limit strict[y/n]: ')
        if isstrict == 'y':
            strict = 'strict'

    newversion.deploy(user, threshold, strict)

    print "------Final State-------"
    printAllUsers(graph)

    plotGraph(graph)

if __name__ == '__main__':
    main(sys.argv)
