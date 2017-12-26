import networkx as nx

from network.Generator import Generator
from network.TieStrength import TieStrength
from reader.CsvReader import CsvReader
from visualization.Monitor import Monitor


class Application:
    networkGenerator = Generator()
    reader = CsvReader()

    nodeList = reader.readEmployee()
    tesekkurList = reader.readRelationship('tesekkur')
    takdirList = reader.readRelationship('takdir')
    dogumgunuList = reader.readRelationship('dogumgunu')

    tieStrength = TieStrength(nodeList, takdirList, dogumgunuList, tesekkurList)

    tieStrengthsFromManagerToEmployee = tieStrength.calculateFromManagerToEmployee()
    tieStrengthsFromEmployeeToEmployee = tieStrength.calculateFromEmployeeToEmployee()

    takdirGraph = networkGenerator.generateGraph(nodeList, takdirList)
    tesekkurGraph = networkGenerator.generateGraph(nodeList, tesekkurList)
    dogumgunuGraph = networkGenerator.generateGraph(nodeList, dogumgunuList)

    betweenness_centrality = nx.betweenness_centrality(takdirGraph)
    closeness_centrality = nx.closeness_centrality(takdirGraph)
    degree_cenrality = nx.degree_centrality(takdirGraph)
    eigenvector_centrality = nx.eigenvector_centrality(takdirGraph)

    monitor = Monitor(nodeList, tesekkurList, takdirList, dogumgunuList)
    monitor.visualizeGraph(tesekkurList)
    monitor.visualizeGraph(takdirList)
    monitor.visualizeGraph(dogumgunuList)

    print("the end")
