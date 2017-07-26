from graph import Digraph, Edge, Node
from ps11 import WeightedEdge, WeightedDigraph
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def buildAll(fileName = "mit_map.txt", test = True):

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

        def nodeExists(name):
            return graphOfMITMap.hasNode(name)

        def addNodeToGraph(name):
            graphOfMITMap.addNode(Node(name))

        def checkThenAddNodeIfFalse(name):
            if nodeExists(name) == False:
                addNodeToGraph(name)

        checkThenAddNodeIfFalse(name)

    def buildThenAddEdge(src, dest, dist, outdoorsDist):

        def edgeExists(src, dest, dist, outdoorsDist):
            print("\nedgeExists running...")
            print("curPath:", curPath)
            print("src, dest, dist, outdoorsDist: {}, {}, {}, {}")
            # return (src, dest) in {(edge.getSource(), edge.getDestination()) for edge in allEdges}
            print(graphOfMITMap.getEdges())
            return graphOfMITMap.hasEdge(src, dest, dist, outdoorsDist)

        def addEdgeToList(src, dest, dist, outdoorsDist):
            print("\naddEdgeToList running...")
            print("curPath:", curPath)
            print("src, dest, dist, outdoorsDist: {}, {}, {}, {}")
            graphOfMITMap.addEdge(WeightedEdge(src, dest, dist, outdoorsDist))

        def checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist):
            print("\ncheckThenAddEdgeIfFalse running...")
            print("curPath:", curPath)
            print("src, dest, dist, outdoorsDist: {}, {}, {}, {}")
            if edgeExists(src, dest, dist, outdoorsDist) == False:
                addEdgeToList(src, dest, dist, outdoorsDist)

        checkThenAddEdgeIfFalse(src, dest, dist, outdoorsDist)


    valGen = getEdgeAndNodeVals(fileName)
    # curPath = valGen.next()

    # def valGenTest(valGen = valGen):
    #     for x in xrange(0, 100):
    #         curPath = valGen.next()
    #         print(curPath)
    # valGenTest()

    def forgetOrBuildEachNode(curPath):
        print("\nforgetOrBuildEachNode running...")
        print("curPath:", curPath)
        buildThenAddNode(curPath[0])
        buildThenAddNode(curPath[1])

    def forgetOrBuildEachEdge(curPath):
        print("\nforgetOrBuildEachEdge running...")
        print("curPath:", curPath)
        src, dest, dist, outdoorsDist = curPath[0], curPath[1], curPath[2], curPath[3]
        buildThenAddEdge(src, dest, dist, outdoorsDist)

    def buildAll(valGen = valGen):
        print("\nbuildAll running...")
        # print("curPath:", curPath)

        def build(func, valGen = valGen):
            counter = 0
            # curPath = valGen.next()
            for curPath in valGen:
            # while curPath != None and counter < 100:
                # nonlocal curPath

                func(curPath = curPath)
                # counter += 1
        build(func = forgetOrBuildEachNode)
        build(func = forgetOrBuildEachEdge)



    # buildAll(func=forgetOrBuildEachEdge)

    def testFunction(func = None, params = None, valCheck = None):
        def buildAndExecuteFunc():
            buildAll()

        def checkValues():
            print("checkValues() running...")
            # for edge in graphOfMITMap.getEdges():
            #     print(edge)
            for node in graphOfMITMap.getNodes():
                print("Node:", node)

            # update a variable like you would with a format, but use a parameter
            # from a function to modify


        checkValues()
        buildAndExecuteFunc()
        # if params == None:
        #     buildAndExecuteFunc()
        checkValues()
    testFunction()

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
