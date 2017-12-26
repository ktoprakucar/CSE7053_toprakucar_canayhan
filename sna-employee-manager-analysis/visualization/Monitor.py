from igraph import *
from igraph.drawing.text import TextDrawer
import cairocffi as cairo

class Monitor:

    def __init__(self, nodeList, takdirList, dogumgunuList, tesekkurList):
        self.nodeList = nodeList
        self.takdirList = takdirList
        self.dogumgunuList = dogumgunuList
        self.tesekkurList = tesekkurList

    def visualizeGraph(self, list):
        g = Graph(directed=True)
        self.constructNodes(g)
        self.constructEdges(g, list)
        self.visualizeElements(g)

    def constructNodes(self, g):
        for line in self.nodeList:
            if line.isManager:
                g.add_vertex(name=line.id, label=line.id, employee="m", color="red")
            else:
                g.add_vertex(name=line.id, label=line.id, employee="e", color="white")

    def constructEdges(self, g, list):
        for line in list:
            if (g.get_eid(line.fromNode, line.toNode, directed=True, error=False) == -1):
                g.add_edge(line.fromNode, line.toNode)
                eid = g.get_eid(line.fromNode, line.toNode)
                edge = g.es[eid]
                edge["weight"] = 1
            else:
                eid = g.get_eid(line.fromNode, line.toNode)
                edge = g.es[eid]
                edge["weight"] += 1

    def visualizeElements(self, g):
        layout = g.layout_auto()
        g.vs["label"] = g.vs["name"]
        visual_style = {}
        visual_style["vertex_label"] = g.vs["name"]
        visual_style["edge_width"] = [1 + 2 * int(weight) for weight in g.es["weight"]]
        visual_style["vertex_size"] = 35
        visual_style["layout"] = layout
        visual_style["bbox"] = (1400, 800)
        visual_style["margin"] = 20
        plot(g, **visual_style)

