from graph import Edge
from ps11 import WeightedEdge



def buildAll(fileName = "mit_map.txt", test = True):

    allNodes = set()
    # testEdge = WeightedEdge(1, 2, 3)
    allEdges = set()

    def getPaths(fileName = "mit_map.txt"):

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
        return allNodes

    def buildThenAddEdge(src, dest, dist, outdoorsDist):

        def edgeExists(src, dest):
            return (src, dest) in {(edge.getSource(), edge.getDestination()) for edge in allEdges}

        def addEdgeToList(src, dest, dist, outdoorsDist):
            allEdges.add(Edge(src, dest, dist, outdoorsDist))

        def checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist):
            if edgeExists(src, dest) == False:
                addEdgeToList(Edge(src, dest, dist, outdoorsDist))

        checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist)

        return allEdges

    curPath = getPaths(fileName).next()
    counter = 0

    def forgetOrBuildEachNode():
        buildThenAddNode(str(curPath[0]))
        buildThenAddNode(str(curPath[1]))

    def buildEachEdge():
        # src, dest, dist, outdoorsDist =
        buildThenAddEdge()

    while curPath != None and counter < 100:
        forgetOrBuildEachNode()
        curPath = getPaths(fileName).next()
        counter += 1

    def testFunction(func = None, params = None, allNodes = allNodes, valCheck = None):
        def buildAndExecuteFunc():
            pass
        def checkValues():
            pass
        print(valCheck)
        if params == None:
            print(WeightedEdge.__mro__)
            # allNodes = addNodeToList(allNodes, 32)
        print(valCheck)
    testFunction(valCheck = allNodes)

# buildAll()

def testClass(valCheck = None):
    print(WeightedEdge.__mro__)

testClass()
# testFunction(valCheck = allNodes)

# for splitLine in mitMapLines:
#     node1, node2 = splitLine[0], splitLine[1]


# How to get the name of the variable
# How to get the params of the function for use in executing another function.

# getPaths("mit_map.txt")
# Use this idea for creating log decorators
