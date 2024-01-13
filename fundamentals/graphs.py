# if no direction between nodes its an undirected graph
# a flight route could be a directed graph because there are certain routes
        #  that a flight has to take between different cities
# in trees there should be only one path beteween 2 nodes, but in graphs there exists multiple paths between nodes
# therefore we can say that tress are a special type of graph


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {} # to make operations more efficient we will use dictionaries
                        # they can help us to assign multiple end values to the same start value
        for start, end in self.edges:
            if start in self.graph_dict: # this will add more value to existing key
                self.graph_dict[start].append(end) # {["New York":['Los Angeles','Las Vegas']]}
            else:
                self.graph_dict[start] = [end] # this will initialize the key/value in the dict
        print('graph dict:' , self.graph_dict)

    def get_path(self, start, end, path = []): # it will return all possible paths between locations
        path += [start]

        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

# you can refer to the pairs of nodes in graphs using tuples
routes =[
    ("New York", "Los Angeles"),
    ("Los Angeles","San Francisco"),
    ("Dallas","Chicago"),
    ('New York', 'Las Vegas')
    
]

# route_graph = Graph(routes)
start = 'New York'
end = 'San Francisco'
# print(route_graph.get_path(start, end))



