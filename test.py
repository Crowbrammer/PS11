from graph import Digraph, Edge, Node
from ps11 import WeightedEdge



def buildAll(fileName = "mit_map.txt", test = True):

    allNodes = set()
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

        def nodeExists(name):
            return name in {node.getName() for node in allNodes}

        def addNodeToList(name):
            allNodes.add(Node(name))

        def checkThenAddNodeIfFalse(name):
            if nodeExists(name) == False:
                addNodeToList(Node(name))

        checkThenAddNodeIfFalse(name)

    def buildThenAddEdge(src, dest, dist, outdoorsDist):

        def edgeExists(src, dest):
            return (src, dest) in {(edge.getSource(), edge.getDestination()) for edge in allEdges}

        def addEdgeToList(src, dest, dist, outdoorsDist):
            allEdges.add(WeightedEdge(src, dest, dist, outdoorsDist))

        def checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist):
            if edgeExists(src, dest) == False:
                addEdgeToList(src, dest, dist, outdoorsDist)

        checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist)

    valGen = getEdgeAndNodeVals(fileName)
    curPath = valGen.next()
    counter = 0

    def forgetOrBuildEachNode():
        print(allNodes)
        buildThenAddNode(curPath[0])
        buildThenAddNode(curPath[1])

    def forgetOrBuildEachEdge():
        src, dest, dist, outdoorsDist = curPath[0], curPath[1], curPath[2], curPath[3]
        buildThenAddEdge(src, dest, dist, outdoorsDist)

    while curPath != None and counter < 100:
        forgetOrBuildEachNode()
        forgetOrBuildEachEdge()
        curPath = valGen.next()
        counter += 1

    def testFunction(func = None, params = None, allNodes = allNodes, valCheck = None):
        def buildAndExecuteFunc():
            pass

        def checkValues():
            print("checkValues() running...")
            for edge in allEdges:
                print(edge)

        checkValues()
        buildAndExecuteFunc()
        # if params == None:
        #     buildAndExecuteFunc()
        checkValues()
    testFunction(valCheck = allNodes)

# buildAll()

# def testClass(valCheck = None):
#     print(WeightedEdge.__mro__)
#
# testClass()

buildAll()

# testFunction(valCheck = allNodes)

# for splitLine in mitMapLines:
#     node1, node2 = splitLine[0], splitLine[1]


# How to get the name of the variable
# How to get the params of the function for use in executing another function.

# getEdgeAndNodeVals("mit_map.txt")
# Use this idea for creating log decorators
