class Node:
    node_list = []
    
    def __init__(self, name):
        self.name = name
        self.node_list.append(self)

    def __repr__(self):
        return self.name

class Directed_Edge(Node):
    edge_list = []

    def __init__(self, name, v1, v2):
        self.name = name
        self.nodes = (v1, v2)
        self.sourse = v1
        self.target = v2
        self.edge_list.append(self)
        
class Edge(Node):
    edge_list = []
    
    def __init__(self, name, v1, v2):
        self.name = name
        self.nodes = (v1, v2)
        self.edge_list.append(self)

class Diraph(Directed_Edge):
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = []
        self.graph = dict()

    def add_node(self, node):
        if not node in self.nodes:
            if type(node) == Node:
                self.nodes.append(node)
                self.graph[node] = []
            else:
                self.nodes

    def add_edge(self, edge):
        if edge.nodes[0] in self.nodes and edge.nodes[1] in self.nodes:
            if not edge in self.edges:
                self.edges.append(edge)
                self.graph[edge.nodes[0]].append(edge.nodes[1])
            else:
                self.edges
        else:
            return "cannot add this edge."

    def adjacent(self, v1, v2):
        return v2 in self.graph[v1]
        
class Graph(Edge):
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = []
        self.graph = dict()

    def add_node(self, node):
        if not node in self.nodes:
            if type(node) == Node:
                self.nodes.append(node)
                self.graph[node] = []
            else:
                self.nodes

    def add_edge(self, edge):
        if edge.nodes[0] in self.nodes and edge.nodes[1] in self.nodes:
            if not edge in self.edges:
                self.edges.append(edge)
                self.graph[edge.nodes[0]].append(edge.nodes[1])
                self.graph[edge.nodes[1]].append(edge.nodes[0])
            else:
                self.edges
        else:
            return "cannot add this edge."

u = Node('u')
v = Node('v')
w = Node('w')
e1 = Directed_Edge('e1', u, v)
g = Diraph('g')
g.add_node(u)
g.add_node(v)
g.add_node(w)
g.add_edge(e1)
