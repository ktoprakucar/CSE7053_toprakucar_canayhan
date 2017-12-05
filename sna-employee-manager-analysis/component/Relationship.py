class Relationship:
    def __init__(self, id, fromNode, toNode, type, point):
        self.id = id
        self.fromNode = fromNode
        self.toNode = toNode
        self.type = type
        self.point = int(point)
