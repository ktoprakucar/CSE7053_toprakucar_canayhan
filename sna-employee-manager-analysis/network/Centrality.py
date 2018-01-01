import networkx as nx

class Centrality:

    def calculateBetweennesCentrality(self, graph):
        undirectedGraph = self.removeEdgeDirectionsAndIsolate(graph)
        return nx.betweenness_centrality(undirectedGraph)

    def calculateClosenessCentrality(self, graph):
        undirectedGraph = self.removeEdgeDirectionsAndIsolate(graph)
        return nx.closeness_centrality(undirectedGraph)

    def calculateDegreeCentrality(self, graph):
        undirectedGraph = self.removeEdgeDirectionsAndIsolate(graph)
        return nx.degree_centrality(undirectedGraph)

    def calculateEigenVectorCentrality(self, graph):
        undirectedGraph = self.removeEdgeDirectionsAndIsolate(graph)
        return nx.eigenvector_centrality(undirectedGraph)

    def removeEdgeDirectionsAndIsolate(self, graph):
        undirectedGraph = graph.to_undirected()
        isolateList = nx.isolates(undirectedGraph)
        for isolate in isolateList:
            print(isolate)
            #undirectedGraph.remove_node(isolate)
        return undirectedGraph