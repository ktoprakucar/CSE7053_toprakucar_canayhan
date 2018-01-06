import networkx as nx
import math


class TieStrength:
    def __init__(self, nodeList, takdirList, dogumgunuList, tesekkurList):
        self.nodeList = nodeList
        self.takdirList = takdirList
        self.dogumgunuList = dogumgunuList
        self.tesekkurList = tesekkurList

    def calculateFromManagerToEmployee(self):
        graph = nx.DiGraph()


        # add takdir
        self.generateGraphFromRelations(graph, self.takdirList, 1 / len(self.takdirList))
        # add tesekkur
        self.generateGraphFromRelations(graph, self.tesekkurList, 1 / len(self.tesekkurList))
        # add dogumgunu
        self.generateGraphFromRelations(graph, self.dogumgunuList, 1 / len(self.dogumgunuList))

        print("before removing nonmanagers: " + str(len(graph.edges)))
        self.removeNonManagerSenders(graph)
        print("before removing nonmanagers: " + str(len(graph.edges)))

        return graph

    def calculateFromEmployeeToEmployee(self):
        graph = nx.DiGraph()

        # add takdir
        self.generateGraphFromRelations(graph, self.takdirList, 1 / len(self.takdirList))
        # add tesekkur
        self.generateGraphFromRelations(graph, self.tesekkurList, 1 / len(self.tesekkurList))
        # add dogumgunu
        self.generateGraphFromRelations(graph, self.dogumgunuList, 1 / len(self.dogumgunuList))

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
        numberOfEdgesFromNode = {}
        self.calculateEdgeNumberFromTheNode(numberOfEdgesFromNode, list)
        greatestWeight = self.getGreatestWeight(list)
        for relation in list:
            normalizedWeight = self.normalizeWeight(relation.point, greatestWeight)
            calculatedWeight = normalizedWeight * (10 / numberOfEdgesFromNode[relation.fromNode]) * calibrationValue
            if graph.has_edge(relation.fromNode, relation.toNode):
                graph[relation.fromNode][relation.toNode]['weight'] += calculatedWeight
                graph[relation.fromNode][relation.toNode]['numberOfEdges'] += 1
            else:
                graph.add_edge(relation.fromNode, relation.toNode, weight= calculatedWeight, numberOfEdges=1)
        mostRelationAmount = self.retrieveMostRelationBetweenSameNodes(graph)
        self.relateEdgeSizeOnWeights(graph, mostRelationAmount)

    def relateEdgeSizeOnWeights(self, graph, mostRelationAmount):
        for edge in graph.edges():
            graph[edge[0]][edge[1]]['weight'] = graph[edge[0]][edge[1]]['weight'] / (
            math.log(graph[edge[0]][edge[1]]['numberOfEdges'] + 1, mostRelationAmount))

    def retrieveMostRelationBetweenSameNodes(self, graph):
        relationAmount = 0
        for edge in graph.edges():
            if graph[edge[0]][edge[1]]['numberOfEdges'] > relationAmount:
                relationAmount = graph[edge[0]][edge[1]]['numberOfEdges']
        return relationAmount

    def getGreatestWeight(self, list):
        greatestWeight = 0
        for relation in list:
            if relation.point > greatestWeight:
                greatestWeight = relation.point
        return greatestWeight

    def normalizeWeight(self, weight, greatestWeight):
        return math.log10(weight + 1) / (math.log10(greatestWeight) + 1)

    def calculateEdgeNumberFromTheNode(self, numberOfEdgesFromNode, list):
        for relation in list:
            if relation.fromNode in numberOfEdgesFromNode:
                numberOfEdgesFromNode[relation.fromNode] += 1
            else:
                numberOfEdgesFromNode[relation.fromNode] = 1
