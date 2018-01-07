import pandas as pd

class Repository:

    def exportListToDataframe(self, betweenness, closeness, degree, eigen):
        df = pd.DataFrame(list(betweenness.items()), columns=['userID', 'betweenness_centrality'])
        df = pd.merge(df, pd.DataFrame(list(closeness.items()), columns=['userID', 'closeness_centrality']), on='userID')
        df = pd.merge(df, pd.DataFrame(list(degree.items()), columns=['userID', 'degree_cenrality']), on='userID')
        df = pd.merge(df, pd.DataFrame(list(eigen.items()), columns=['userID', 'eigenvector_centrality']), on='userID')
        return df

    def exportGraphToDataframe(self, graph):
        index = 0
        df = pd.DataFrame(columns=['from_node', 'to_node', 'tie_strenght'])
        for edge in graph.edges():
            df.loc[index] = [edge[0],edge[1],graph[edge[0]][edge[1]]['weight']]
            index += 1
        return df
