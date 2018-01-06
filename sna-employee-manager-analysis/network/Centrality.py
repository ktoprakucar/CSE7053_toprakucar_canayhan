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
        undirectedGraph = self.retrieveMostCrowdedComponent(graph)
        return undirectedGraph

    def retrieveMostCrowdedComponent(self, graph):
        un = graph.to_undirected()
        components = list(nx.connected_component_subgraphs(un))
        mostCrowdedId = 0
        mostCrowdedPopulation = 0
        if len(components) > 1:
            for g in components:
                if len(g.nodes) > mostCrowdedPopulation:
                    mostCrowdedPopulation = len(g.nodes)
                    mostCrowdedId = components.index(g)
        undirectedGraph = components[mostCrowdedId]
        return undirectedGraph
