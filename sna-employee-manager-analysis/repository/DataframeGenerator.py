import pandas as pd

class Repository:

    def exportToDataframe(self, betweenness, closeness, degree, eigen):
        df = pd.DataFrame(list(betweenness.items()), columns=['userID', 'betweenness_centrality'])
        df = pd.merge(df, pd.DataFrame(list(closeness.items()), columns=['userID', 'closeness_centrality']), on='userID')
        df = pd.merge(df, pd.DataFrame(list(degree.items()), columns=['userID', 'degree_cenrality']), on='userID')
        df = pd.merge(df, pd.DataFrame(list(eigen.items()), columns=['userID', 'eigenvector_centrality']), on='userID')
        return df
