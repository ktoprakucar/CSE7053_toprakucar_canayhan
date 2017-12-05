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

    print(len(tesekkurList))
    print(len(takdirList))
    print(len(dogumgunuList))

    takdirGraph = networkGenerator.generateGraph(nodeList, takdirList)
    tesekkurGraph = networkGenerator.generateGraph(nodeList, tesekkurList)
    dogumgunuGraph = networkGenerator.generateGraph(nodeList, dogumgunuList)

    print(takdirGraph.number_of_edges())
    print(tesekkurGraph.number_of_edges())
    print(dogumgunuGraph.number_of_edges())

    #betweenness_centrality = nx.betweenness_centrality(graph)
    #closeness_centrality = nx.closeness_centrality(graph)
    #degree_cenrality = nx.degree_centrality(graph)
    #eigenvector_centrality = nx.eigenvector_centrality(graph)


