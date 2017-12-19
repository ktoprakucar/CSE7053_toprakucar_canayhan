import networkx as nx


class TieStrength:
    def __init__(self, nodeList, takdirList, dogumgunuList, tesekkurList):
        self.nodeList = nodeList
        self.takdirList = takdirList
        self.dogumgunuList = dogumgunuList
        self.tesekkurList = tesekkurList

    def calculateFromManagerToEmployee(self):
        graph = nx.DiGraph()

        # add takdir
        self.generateGraphFromRelations(graph, self.takdirList, 1000)
        # add tesekkur
        self.generateGraphFromRelations(graph, self.tesekkurList, 1 / 5)
        # add dogumgunu
        self.generateGraphFromRelations(graph, self.dogumgunuList, 1)

        print("before removing nonmanagers: " + str(len(graph.edges)))
        self.removeNonManagerSenders(graph)
        print("before removing nonmanagers: " + str(len(graph.edges)))

        return graph

    def calculateFromEmployeeToEmployee(self):
        graph = nx.DiGraph()

        # add takdir
        self.generateGraphFromRelations(graph, self.takdirList, 1000)
        # add tesekkur
        self.generateGraphFromRelations(graph, self.tesekkurList, 1 / 5)
        # add dogumgunu
        self.generateGraphFromRelations(graph, self.dogumgunuList, 1)

        print("before removing managers: " + str(len(graph.edges)))
        self.removeManagerSenders(graph)
        print("before removing managers: " + str(len(graph.edges)))

        return graph

    def removeNonManagerSenders(self, graph):
        edges = list(graph.edges())
        for edge in edges:
            isManager = True
            for node in self.nodeList:
                if node.id == edge[0]:
                    isManager = node.isManager
                    break
            if not isManager:
                graph.remove_edge(edge[0], edge[1])

    def removeManagerSenders(self, graph):
        edges = list(graph.edges())
        for edge in edges:
            isManager = True
            for node in self.nodeList:
                if node.id == edge[0]:
                    isManager = node.isManager
            if isManager:
                graph.remove_edge(edge[0], edge[1])

    def generateGraphFromRelations(self, graph, list, calibrationValue):
        for relation in list:
            if graph.has_edge(relation.fromNode, relation.toNode):
                graph[relation.fromNode][relation.toNode]['weight'] += relation.point / calibrationValue
            else:
                graph.add_edge(relation.fromNode, relation.toNode, weight=relation.point / calibrationValue)
