import networkx as nx
import math


class TieStrength:
    def __init__(self, nodeList, takdirList, dogumgunuList, tesekkurList):
        self.nodeList = nodeList
        self.takdirList = takdirList
        self.dogumgunuList = dogumgunuList
        self.tesekkurList = tesekkurList

    def calculateFromManagerToEmployee(self):
        # add takdir
        takdirGraph = self.generateGraphFromRelations(self.takdirList, 1 / len(self.takdirList))
        # add tesekkur
        tesekkurGraph = self.generateGraphFromRelations(self.tesekkurList, 1 / len(self.tesekkurList))
        # add dogumgunu
        dogumgunuGraph = self.generateGraphFromRelations(self.dogumgunuList, 1 / len(self.dogumgunuList))

        graphlist = [takdirGraph, tesekkurGraph, dogumgunuGraph]
        graph = self.mergeGraphs(graphlist)
        self.removeNonManagerSenders(graph)

        return graph

    def calculateFromEmployeeToEmployee(self):
        # add takdir
        takdirGraph = self.generateGraphFromRelations(self.takdirList, 1 / len(self.takdirList))
        # add tesekkur
        tesekkurGraph = self.generateGraphFromRelations(self.tesekkurList, 1 / len(self.tesekkurList))
        # add dogumgunu
        dogumgunuGraph = self.generateGraphFromRelations(self.dogumgunuList, 1 / len(self.dogumgunuList))

        graphlist = [takdirGraph, tesekkurGraph, dogumgunuGraph]
        graph = self.mergeGraphs(graphlist)
        self.removeManagerSenders(graph)

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

    def generateGraphFromRelations(self, list, calibrationValue):
        graph = nx.Graph()
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
        return graph

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

    def mergeGraphs(self, graphlist):
        graph = nx.Graph()
        for g in graphlist:
            for edge in g.edges():
                if graph.has_edge(edge[0], edge[1]):
                    graph[edge[0]][edge[1]]['weight'] += g[edge[0]][edge[1]]['weight']
                else:
                    graph.add_edge(edge[0], edge[1], weight=g[edge[0]][edge[1]]['weight'])
        return graph
