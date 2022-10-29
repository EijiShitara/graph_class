class Node:

    node_list = []
    
    def __init__(self, name):
        self.name = name
        self.node_list.append(self)

class Edge(Node):

    edge_list = []
    
    def __init__(self, name, v1, v2, w=0):
        self.name = name
        self.nodes = (v1.name, v2.name)
        self.node_objs = (v1, v2)
        self.weight = w
        self.edge_list.append(self)
        
class Graph(Edge):
    
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = []
        
        self.node_objs = []
        self.edge_objs = []

    def add_node(self, node):
        if not node.name in self.nodes:
            self.nodes.append(node.name)
            self.node_objs.append(node)
        else:
            self.nodes

    def add_edge(self, edge):
        if edge.nodes[0] in self.nodes and edge.nodes[1] in self.nodes:
            self.edges.append(edge.name)
            self.edge_objs.append(edge)
        else:
            return "cannot add this edge."

    def adjacency(self):
        adj_obj_dict = dict()
        adj_dict = dict()
        
        for v in self.node_objs:
            adj_obj_dict[v] = []
            adj_dict[v.name] = []
            
            for e in self.edge_objs:
                if e.node_objs[0] == v:
                    adj_obj_dict[v].append(e.node_objs[1])
                    adj_dict[v.name].append(e.nodes[1])
                if e.node_objs[1] == v:
                    adj_obj_dict[v].append(e.node_objs[0])
                    adj_dict[v.name].append(e.nodes[0])

        return adj_dict


#generating 5 vertices.
node_obj_list = []
for i in range(5):
    code1 = 'v{} = Node("v{}")'.format(i, i)
    exec(code1)
    code2 = 'node_obj_list.append(v{})'.format(i)
    exec(code2)

node_name_list = []
for i in node_obj_list:
    node_name_list.append(i.name)
    

#generating edges.
edge_obj_list = []
for i in range(len(node_obj_list)):
    for j in range(i+1, len(node_obj_list)):
        code1 = 'e{}{} = Edge("e{}{}", v{}, v{})'.format(i, j, i, j, i, j)
        exec(code1)
        code2 = 'edge_obj_list.append(e{}{})'.format(i, j)
        exec(code2)

edge_name_list = []
for i in edge_obj_list:
    edge_name_list.append(i.name)

#assigng a random weight to each edge.
import random
for e in Edge.edge_list:
    e.weight = random.randint(0, 100)
    print(e.weight)

#creating a complete graph with 5 nodes.     
g = Graph('g')

for i in node_obj_list:
    g.add_node(i)

for i in edge_obj_list:
    g.add_edge(i)
