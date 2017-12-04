from network.Generator import Generator
from reader.CsvReader import CsvReader

import networkx as nx

class Application:
    networkGenerator = Generator()
    reader = CsvReader()

    nodeList = reader.readEmployee()
    tesekkurList = reader.readRelationship('tesekkur')
    takdirList = reader.readRelationship('takdir')
    dogumgunuList = reader.readRelationship('dogumgunu')
    relationships = tesekkurList + takdirList + dogumgunuList

    graph = networkGenerator.generateGraph(nodeList, relationships)

    print(graph.number_of_nodes())
    print(graph.number_of_edges())

