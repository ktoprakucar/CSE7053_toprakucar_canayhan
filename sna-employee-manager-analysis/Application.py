import networkx as nx

from network.Centrality import Centrality
from network.Generator import Generator
from network.TieStrength import TieStrength
from reader.CsvReader import CsvReader
from visualization.Monitor import Monitor


class Application:
    networkGenerator = Generator()
    reader = CsvReader()
    centrality = Centrality()

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

    betweenness_centrality = centrality.calculateBetweennesCentrality(takdirGraph)
    closeness_centrality = centrality.calculateClosenessCentrality(takdirGraph)
    degree_cenrality = centrality.calculateDegreeCentrality(takdirGraph)
    eigenvector_centrality = centrality.calculateEigenVectorCentrality(takdirGraph)

    monitor = Monitor(nodeList, tesekkurList, takdirList, dogumgunuList)
    monitor.visualizeGraph(tesekkurList)
    monitor.visualizeGraph(takdirList)
    monitor.visualizeGraph(dogumgunuList)

    print("the end")
