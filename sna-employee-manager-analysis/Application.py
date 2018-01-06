from repository.DataframeGenerator import Repository
from network.Centrality import Centrality
from network.Generator import Generator
from network.TieStrength import TieStrength
from reader.CsvReader import CsvReader
from visualization.Monitor import Monitor


class Application:
    networkGenerator = Generator()
    reader = CsvReader()
    centrality = Centrality()
    repository = Repository()

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

    takdir_dataframe = repository.exportToDataframe(takdir_betweenness_centrality, takdir_closeness_centrality, takdir_degree_cenrality, takdir_eigenvector_centrality)
    tesekkur_dataframe = repository.exportToDataframe(tesekkur_betweenness_centrality, tesekkur_closeness_centrality, tesekkur_degree_cenrality, tesekkur_eigenvector_centrality)
    dogumgunu_dataframe = repository.exportToDataframe(dogumgunu_betweenness_centrality, dogumgunu_closeness_centrality, dogumgunu_degree_cenrality, dogumgunu_eigenvector_centrality)

    print(takdir_dataframe)
    print(tesekkur_dataframe)
    print(dogumgunu_dataframe)

    monitor = Monitor(nodeList, tesekkurList, takdirList, dogumgunuList)
    monitor.visualizeGraph(tesekkurList)
    monitor.visualizeGraph(takdirList)
    monitor.visualizeGraph(dogumgunuList)

    print("the end")
