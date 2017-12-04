import networkx as nx

class Generator:

    def generateGraph(self, nodeList, relationshipList):
        graph = nx.MultiDiGraph()
        for node in nodeList:
            graph.add_node(node.id)
        for r in relationshipList:
            graph.add_edge(r.fromNode, r.toNode, type=r.type)
        return graph