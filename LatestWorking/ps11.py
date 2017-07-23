from graph import Edge

class WeightedEdge(Edge):
    """docstring for WeightedEdge."""
    def __init__(self, src, dest, dist, outdoorsDist):
        super(WeightedEdge, self).__init__(src, dest)
        self.totalDist = dist
        self.outdoorsDist = outdoorsDist
    def getWeight():
        return self.self.totalDist, self.outdoorsDist
