# 6.00 Problem Set 11
#
# ps11.py
#
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string, time
from graph import Digraph, Edge, Node

start_time = time.time()

class WeightedEdge(Edge):
    """docstring for WeightedEdge."""
    def __init__(self, src, dest, dist, outdoorsDist):
        super(WeightedEdge, self).__init__(src, dest)
        self.totalDist = dist
        self.outdoorsDist = outdoorsDist
    def getDistances(self):
        return self.totalDist, self.outdoorsDist

class WeightedDigraph(Digraph):
    """docstring for WeightedDigraph."""
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if src is None or dest is None:
            raise ValueError("src from WeightedDigraph: {}".format(src))
        totalDist, outdoorsDist = edge.getDistances()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest, totalDist, outdoorsDist))
    def hasNode(self, nodeName):
        return nodeName in {node.getName() for node in self.nodes}
    def hasEdge(self, src, dest, dist, outdoorsDist):
        return (dest, dist, outdoorsDist) in self.edges.values()
    def getNodes(self):
        return self.nodes
    def getEdges(self):
        return self.edges


#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph)
#
# Each node represents a building. Each edge is the path between the building.
# Each unique 1st and 2nd value from each line in the mit_map file will be a node
# in the node set. Each line in the mit_map file will be an edge. The idea will be,
# while accumulating total distance and distance outdoors, to follow the edge at
# each point, until the src == the desired output. Need:
#
#  - knowledge of search methods implementation
#  - way of preventing cycles (if the path exists before, take a diff path or stop)




def load_map(fileName = "mit_map.txt", test = True):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    #TODO
    print "Loading map from file..."
    graphOfMITMap = WeightedDigraph()
    # allNodes = set()
    allEdges = set()

    def getEdgeAndNodeVals(fileName = "mit_map.txt"):
        """
        Generator takes a file of lines organized like:
            13 20 32 500
            1234 12 53 1353
        Takes a line from the data set.
        Splits it into a tuple of unique values, delimited by a space
        Removes the "\n" from a bunch of the 4th (outdoorsDist) values
        Yields the next tuple of paths each time its called
        """

        def valWithoutNewline(val):
            return val.replace("\n", "")

        with open(fileName) as f:
            for line in f:
                splitLine = line.split(" ")
                splitLine[3] = valWithoutNewline(splitLine[3])
                yield splitLine

    def buildThenAddNode(name):
        # print "\n      buildThenAddNode running..."

        def nodeExists(name):
            # print "\n          nodeExists running..."
            return graphOfMITMap.hasNode(name)

        def addNodeToGraph(name):
            # print "\n          addNodeToGraph running..."
            currNode = Node(name)
            # print("currNode:", currNode)
            graphOfMITMap.addNode(currNode)
            return currNode

        def checkThenAddNodeIfFalse(name):
            # print "\n        checkThenAddNodeIfFalse running..."
            if nodeExists(name) == False:
                # print("\ncheckThenAddNodeIfFalse running...")

                currNode = addNodeToGraph(name)
                # print("currNode:", currNode)
                return currNode
            else:
                currNode = ""
                for node in graphOfMITMap.getNodes():
                    if node.getName() == name:
                        currNode = node
                return currNode#[node if node.getName() == name for node in graphOfMITMap.getNodes()][0]


        nodeName = checkThenAddNodeIfFalse(name)
        # print "\n      nodeName: {}".format(nodeName)
        return nodeName

    def buildThenAddEdge(src, dest, dist, outdoorsDist):
        # print("\n      buildThenAddEdge running...")

        def edgeExists(src, dest, dist, outdoorsDist):
            # print "\n          edgeExists running..."
            # print "          src, dest, dist, outdoorsDist: {}, {}, {}, {}".format(src, dest, dist, outdoorsDist)
            # return (src, dest) in {(edge.getSource(), edge.getDestination()) for edge in allEdges}
            # print "          graphOfMITMap.getNodes()", [node.getName() for node in graphOfMITMap.getNodes()]
            return graphOfMITMap.hasEdge(src, dest, dist, outdoorsDist)

        def addEdgeToGraph(src, dest, dist, outdoorsDist):
            # print "\n          addEdgeToGraph running..."
            # print "          src, dest, dist, outdoorsDist: {}, {}, {}, {}".format(src, dest, dist, outdoorsDist)

            # print("id(src), id(dest)", id(src), id(dest))
            graphOfMITMap.addEdge(WeightedEdge(src, dest, dist, outdoorsDist))

        def checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist):
            # print "\n        checkThenAddEdgeIfFalse running..."
            # print "        src, dest, dist, outdoorsDist: {}, {}, {}, {}".format(src, dest, dist, outdoorsDist)

            if edgeExists(src, dest, dist, outdoorsDist) == False:
                addEdgeToGraph(src, dest, dist, outdoorsDist)

        checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist)


    valGen = getEdgeAndNodeVals(fileName)
    # curPath = valGen.next()

    # def valGenTest(valGen = valGen):
    #     for x in xrange(0, 100):
    #         curPath = valGen.next()
    #         print(curPath)
    # valGenTest()



    def forgetOrBuildEachNodeAndEdge(curPath):
        # print "\n    forgetOrBuildEachNodeAndEdge running..."
        # print "    curPath: {}".format(curPath)
        src = buildThenAddNode(curPath[0])
        dest = buildThenAddNode(curPath[1])
        # print "    id({}), id({})".format(id(src), id(dest))
        dist, outdoorsDist = curPath[2], curPath[3]
        # print "    src, dest, dist, outdoorsDist: {}, {}, {}, {}".format(src, dest, dist, outdoorsDist)
        buildThenAddEdge(src, dest, dist, outdoorsDist)

    def buildAll(valGen = valGen):
        # print("\nbuildAll running...")
        # print("curPath:", curPath)

        def build(func, valGen = valGen):
            # print("\n  build running...")
            counter = 0
            # curPath = valGen.next()
            for curPath in valGen:
            # while curPath != None and counter < 100:
                # nonlocal curPath

                func(curPath = curPath)
                # counter += 1
        build(func = forgetOrBuildEachNodeAndEdge)

    buildAll()

    # def testFunction(func = None, params = None, valCheck = None):
    #     def buildAndExecuteFunc():
    #         buildAll()
    #
    #     def checkValues():
    #         print("checkValues() running...")
    #         # for edge in graphOfMITMap.getEdges():
    #         #     print(edge)
    #         for node in graphOfMITMap.getNodes():
    #             print("Node:", node)
    #
    #         # update a variable like you would with a format, but use a parameter
    #         # from a function to modify
    #
    #
    #     checkValues()
    #     buildAndExecuteFunc()
    #     # if params == None:
    #     #     buildAndExecuteFunc()
    #     checkValues()
    # testFunction()

    return graphOfMITMap


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints

# Minimize the time spent outdoors, using only a path in the graph from point A to
# point
# # TODO:
#

def bruteForceSearch(digraph, start, dest, maxTotalDist, maxDistOutdoors, optimized=False):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    # NOTE: I want it to return ALL complete paths.
    #TODO
    printNames = True
    for node in digraph.getNodes():
        if str(start) == node.getName():
            start = node
        elif str(dest) == node.getName():
            dest = node

    completedPaths = set()
    allPaths = []

    def search(path = [start]):

        parentNode = path[-1:][0]

        def printNames(path, parentNode, child):
            print "\nPath:"
            for i in xrange(len(path)):
                print "{}:".format(i), path[i].getName()
            print "\nParent Node:", parentNode
            print "\nChild Nodes:"
            for child in digraph.childrenOf(parentNode):
                # print "child[0].getName():", child[0].getName()
                print "Child of Node {}: {}".format(parentNode.getName(), child[0].getName())


        def printStart():
            print "\nNode: {}".format(parentNode.getName())
            print "\nChild Nodes:"
            for child in digraph.childrenOf(parentNode):
                # print "child[0].getName():", child[0].getName()
                print "Child of Node {}: {}".format(parentNode.getName(), child[0].getName())

        # printStart()

        for childNode in digraph.childrenOf(parentNode):
            # print "childNode[0], dest:", childNode[0], dest
            if childNode[0] not in path: # Don't understand in, not, and __eq__
                if childNode[0] == dest:
                    # Modifier method
                    # completedPath = path + [childNode] # This may modify the
                    # completePaths += completedPath
                    # Pure method
                    completedPath = path + [childNode[0]]
                    completedPaths.add(tuple(completedPath)) # This tuple is pretty messy. Am I adding what I* want to add?
                    allPaths.append(completedPath)

                    # print "Completed path added to completedPaths:", completedPath
                    # return path + [childNode[0]] #, nodesSeen # At each frame, return the current path and whether it's a match or not.
                elif completedPaths and optimized:
                    if len(min(completedPaths)) > len(path + [childNode[0]]):
                        continue
                else: # Has children (that are not in the path)
                    # if None

                    # printNames(path, parentNode, childNode)
                    if digraph.childrenOf(childNode[0]):
                        nextPath = path + [childNode[0]]
                        if nextPath not in allPaths:
                            allPaths.append(nextPath)
                            childPath = search(path = path + [childNode[0]])
                            # if childPath:
                                # print "childPath has a completedPath"
                    # else:
                        # print "No children nodes for node {}".format(parentNode.getName())
            # else:
                # print "childNode[0] in path: {} in {}".format(childNode[0], [node.getName() for node in path])
                # raw_input()
        if not completedPaths:
            return "No path from start node to dest node detected..."
        elif printNames and completedPaths:
            return [[node.getName() for node in tuplePath] for tuplePath in completedPaths]
        else:
            return completedPaths

    return search()



#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, dest, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    return bruteForceSearch(digraph, start, dest, maxTotalDist, maxDistOutdoors, optimized=True)

print "Result of my function:", directedDFS(load_map(), 32, 56, 100, 100)
print "My program took", time.time() - start_time, "to run"
# Test
# # Uncomment below when ready to test
# if __name__ == '__main__':
#     # Test cases
#     digraph = load_map("mit_map.txt")
#
#     LARGE_DIST = 1000000
#
#     # Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#
#     # Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#
#     # Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#
#     # Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#
#     # Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#
#     # Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#
#     # Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#
#     try:
#         directedDFS(digraph, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
#
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
#
#     # Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#
#     try:
#         directedDFS(digraph, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
#
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
