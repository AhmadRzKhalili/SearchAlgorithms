from functools import reduce


NODE1 = "NODE1"
NODE2 = "NODE2"
VAL = "LENGTH"


class Edge:
    def __init__(self, node1, node2, length=1):
        self.node1 = node1
        self.node2 = node2
        self.length = length

    @classmethod
    def fromdict(cls, edgedict):
        return cls(node1=edgedict['NODE1'], node2=edgedict['NODE2'], length=edgedict['LENGTH'])

    def __repr__(self):
        return "Edge from " + self.node1 + " to "+self.node2 + " with length "+str(self.length)

    def __eq__(self, __o: object) -> bool:
        return ((self.node1 == __o.node1 or self.node1 == __o.node2)
                and (self.node2 == __o.node1 or self.node2 == __o.node2))


class Graph:
    def __init__(self, nodes=None, edges=None, heuristic=None):
        self.edges = []
        if edges:
            self.edges = edges
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = list(
                set([e.node1 for e in self.edges]+[e.node2 for e in self.edges]))
        self.heuristic = {}
        if heuristic:
            self.heuristic = heuristic
        self.validate()

    def validate(self):
        assert len(self.nodes) == len(set(self.nodes)), "no duplicate nodes"
        for node in self.nodes:
            connected = self.get_connected_nodes(node)
            assert len(connected) == len(set(connected)
                                         ), "no duplicate edges "+str(connected)+" in node "+str(node)
        for edge in self.edges:
            assert (edge.node1 in self.nodes)
            assert (edge.node2 in self.nodes)
            assert edge.length > 0
        for start in self.nodes:
            for goal in self.nodes:
                assert self.get_heuristic(start, goal) >= 0

    def get_heuristic(self, start, goal):
        assert start in self.nodes, start+" node not in graph "+str(self)
        assert goal in self.nodes, goal+" node not in graph "+str(self)
        if goal in self.heuristic:
            if start in self.heuristic[goal]:
                return self.heuristic[goal][start]
            else:
                return 0
        else:
            return 0

    def get_edge(self, node1, node2):
        assert node1 in self.nodes, node1+" node not in graph "+str(self)
        assert node2 in self.nodes, node2+"node not in graph "+str(self)
        for edge in self.edges:
            if edge == Edge(node1, node2):
                return edge

    def get_connected_nodes(self, node):
        assert node in self.nodes, "node " + node + " not in graph "+str(self)
        result = [e.node1 for e in self.edges if e.node2 == node] + \
            [e.node2 for e in self.edges if e.node1 == node]
        return sorted(result)

    def are_connected(self, node1, node2):
        return bool(self.get_edge(node1, node2))

    def is_valid_path(self, path):
        def is_valid_path_reducer(a, b):
            if a == False or not self.are_connected(a, b):
                return False
            else:
                return b
        return bool(reduce(is_valid_path_reducer, path))

    def add_edge(self, edge):
        if edge.node1 not in self.nodes:
            self.nodes.append(edge.node1)
        if edge.node2 not in self.nodes:
            self.nodes.append(edge.node2)
        self.edges.append(edge)

    def set_heuristic(self, start, goal, value):
        if goal not in self.heuristic:
            self.heuristic[goal] = {}
        self.heuristic[goal][start] = value

    def __str__(self):
        return "Graph: \n  edges="+str(self.edges)+"\n  heuristic="+str(self.heuristic)
