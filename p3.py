import networkx as nx

def my_diameter(graph):

    #validate that graph is connected
    if nx.is_connected(graph) == False:
        print ("ERROR: Graph is not connected")
        return -1

    nodes = graph.nodes()
    s_paths = []

    #loops through every node and every consecutive node
    for node in nodes:
        for consec_node in nodes:
            if node == consec_node:
                continue
            
            #append to a list the shortest path of every node combination
            s_paths.append(len(nx.shortest_path(graph, source = node, target = consec_node)) - 1)
                                   
    #return the highest shortest path
    return max(s_paths)


g = nx.cycle_graph(5)

#g = nx.Graph({0:[1,2], 3:[]})
print nx.diameter(g)
print my_diameter(g)
