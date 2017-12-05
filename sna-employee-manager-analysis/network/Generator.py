import networkx as nx


class Generator:
    def generateGraph(self, nodeList, relationshipList):
        graph = nx.DiGraph()
        for node in nodeList:
            graph.add_node(node.id)
        for r in relationshipList:
            if graph.has_edge(r.fromNode, r.toNode):
                graph[r.fromNode][r.toNode]['weight'] += r.point
            else:
                graph.add_edge(r.fromNode, r.toNode, weight=r.point)
        return graph
