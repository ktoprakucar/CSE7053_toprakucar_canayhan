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

    takdir_betweenness_centrality = centrality.calculateBetweennesCentrality(takdirGraph)
    takdir_closeness_centrality = centrality.calculateClosenessCentrality(takdirGraph)
    takdir_degree_cenrality = centrality.calculateDegreeCentrality(takdirGraph)
    takdir_eigenvector_centrality = centrality.calculateEigenVectorCentrality(takdirGraph)

    tesekkur_betweenness_centrality = centrality.calculateBetweennesCentrality(tesekkurGraph)
    tesekkur_closeness_centrality = centrality.calculateClosenessCentrality(tesekkurGraph)
    tesekkur_degree_cenrality = centrality.calculateDegreeCentrality(tesekkurGraph)
    tesekkur_eigenvector_centrality = centrality.calculateEigenVectorCentrality(tesekkurGraph)

    dogumgunu_betweenness_centrality = centrality.calculateBetweennesCentrality(dogumgunuGraph)
    dogumgunu_closeness_centrality = centrality.calculateClosenessCentrality(dogumgunuGraph)
    dogumgunu_degree_cenrality = centrality.calculateDegreeCentrality(dogumgunuGraph)
    dogumgunu_eigenvector_centrality = centrality.calculateEigenVectorCentrality(dogumgunuGraph)

    monitor = Monitor(nodeList, tesekkurList, takdirList, dogumgunuList)
    monitor.visualizeGraph(tesekkurList)
    monitor.visualizeGraph(takdirList)
    monitor.visualizeGraph(dogumgunuList)

    print("the end")
