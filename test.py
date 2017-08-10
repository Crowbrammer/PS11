import string
from graph import Digraph, Edge, Node
from ps11 import WeightedEdge, WeightedDigraph

def bruteForceSearch(digraph, start, dest, maxTotalDist, maxDistOutdoors):
    """
    This is a function that should implement itself many times. The ultimate in
    economy. The self-perpetuating machine.
    """
    for node in digraph.getNodes():
        if str(start) == node.getName():
            start = node
        elif str(dest) == node.getName():
            dest = node

    def search(path = [start], completedPaths = set()):
        for childNode in digraph.childrenOf(path[-1:]):
            if childNode not in path:
                if childNode == dest:
                    # Modifier method
                    # completedPath = path + [childNode] # This may modify the
                    # completePaths += completedPath
                    # Pure method
                    return path + [childNode], completedPaths.add((path + [childNode])) #, nodesSeen # At each frame, return the current path and whether it's a match or not.
                else: # Has children (that are not in the path)
                    # if None
                    if childNode.childrenOf():
                        return search(path = path + [childNode], completedPaths = completedPaths) #, nodesSeen)
                    else:
                        print "No children nodes for node {}".format(path[-1:].getName())
        if not completedPaths:
            return "No path from start node to dest node exists..."
        else:
            return completedPaths
    return search()

bruteForceSearch(load)
    # Doesn't return anything if it reaches a node with no childNodes not in the paths
    # Where do I* handle the None returns in these types of situations?
    # Doesn't return anything if it reaches a node with no childNodes, period.

def testSets(set1, set2):
    # set1 = {node.getName() for node in set1}
    # set2 = {node.getName() for node in set2}
    # print "\ntype(set1), type(set2):\n", type(set1), type(set2)
    print "\nset1:\n", set1
    print "\nset2:\n", set2
    print "\nset1 - set2:\n", set1 - set2
    print "min({set1, set2}):", min(set1, set2)
    # print "\nset1 in set2:\n", set1 in set2
    # print "\nset1 not in set2:\n", set1 not in set2
    # print "\nset1.issubset(set2):\n", set1.issubset(set2)
    # print "\nset1.issuperset(set2):\n", set1.issuperset(set2)
    # print "\nset1.union(set2):\n", set1.union(set2)
    # print "\nset1.intersection(set2):\n", set1.intersection(set2)
    # print "\nset1.difference(set2):\n", set1.difference(set2)
    # if not set1.difference(set2):
    #     print "Works"
    # print "\nset1.symmetric_difference(set2):\n", set1.symmetric_difference(set2)
    # print "\nset1.copy():\n", set1.copy()

testVisited = {1, 2, 3, 4}
testChildren = {1, 2}
testSets(testVisited, testChildren)
testSets(testChildren, testVisited)
assert False, 'testSets run'

# When it hits a dead end with no completedPath
#

# I want footnoted marks that let me keep notes on the code, and quickly visited
# where I was talking about. Like hypothes.is
