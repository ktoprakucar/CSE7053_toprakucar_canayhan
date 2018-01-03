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
        undirectedGraph = nx.Graph();
        edges = list(graph.edges())
        for edge in edges:
            undirectedGraph.add_edge(edge[0], edge[1])
        print("normal graph: ")
        print(str(len(graph.nodes)))
        print("isolated graph: ")
        print(str(len(undirectedGraph.nodes)))


        return undirectedGraph