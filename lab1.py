from typing import List
from graph import Edge, Graph


def path_edges(graph: Graph, path) -> List[Edge]:
    edges = []

    for i in range(len(path) - 1):
        edge = graph.get_edge(path[i], path[i + 1])
        edges.append(edge)

    return edges


def path_length(graph, path) -> int:
    cost = 0

    for i in range(len(path) - 1):
        edge = graph.get_edge(path[i], path[i + 1])
        cost += edge.length

    return cost


# Implement the following algorithms:


def bfs(graph: Graph, start, goal):
    agenda = []
    agenda.append([start])
    
    while len(agenda) != 0:
        path = agenda.pop(0)
        node = path[-1]

        if node == goal:
            print(agenda, end="\n\n")
            return path
                    

        neighbors = graph.get_connected_nodes(node)

        for n in neighbors:
            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)
                agenda.append(path_copy)
                    
        
        print(agenda,  end="\n\n")

    return []


def dfs(graph: Graph, start, goal):
    agenda = []
    agenda.append([start])
    
    while len(agenda) != 0:
        path = agenda.pop(0)
        node = path[-1]

        if node == goal:
            print(agenda, end="\n\n")
            return path

        neighbors = graph.get_connected_nodes(node)

        extended_nodes = []

        for n in neighbors:

            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)
                extended_nodes.append(path_copy)
                # agenda.insert(0, path_copy)            

                    
        extended_nodes = extended_nodes[::-1]
        for extended_node in extended_nodes:
            agenda.insert(0, extended_node)       
        
        print(agenda,  end="\n\n")

    return []


def ids(graph: Graph, start, goal):
    agenda = []
    agenda.append([start])

    level = 0

    # checking with level_limit = 0
    if start == goal:
        return [start]
    
    print(agenda,  end="\n\n")
    
    for level_limit in range(1, len(graph.nodes)):
        agenda = []
        agenda.append([start])
        level = 0

        while len(agenda) != 0:
            print("--------------------------------")
            print(agenda,  end="\n\n")
            print(level)

            path = agenda.pop(0)
            node = path[-1]
            
            if node == goal:
                print(agenda, end="\n\n")
                return path

            neighbors = graph.get_connected_nodes(node)
            level += 1

            if level > level_limit:
                if len(agenda) == 0:
                    break
                else:
                    path = agenda.pop(0)
                    level = len(path) - 1
                    agenda.insert(0, path)
                    continue

            extended_nodes = []

            for n in neighbors:

                if n not in path:
                    path_copy = path.copy()
                    path_copy.append(n)
                    extended_nodes.append(path_copy)
                    # agenda.insert(0, path_copy)            

            extended_nodes = extended_nodes[::-1]
            for extended_node in extended_nodes:
                agenda.insert(0, extended_node)       
            

    return []


def hill_climbing(graph: Graph, start, goal):
    agenda = []
    agenda.append([graph.get_heuristic(start, goal), start])
    print(agenda, end="\n\n")
    
    while len(agenda) != 0:

        path = agenda.pop(0)
        node = path[-1]

        if node == goal:
            print(agenda, end="\n\n")
            return path[1:]

        neighbors = graph.get_connected_nodes(node)
        
        extended_nodes = []

        for n in neighbors:
            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)

                h =  graph.get_heuristic(n, goal)
                
                path_copy[0] = h
                extended_nodes.append(path_copy)

        extended_nodes = extended_nodes[::-1]
        extended_nodes = sorted(extended_nodes, key=lambda x: (x[0]))
        for i in range(len(extended_nodes)):
            extended_node = extended_nodes.pop(-1)
            agenda.insert(0, extended_node)       
    

        print(agenda, end="\n\n")

    return []


def beam_search(graph: Graph, start, goal, beam_width):
    agenda = []
    agenda.append([graph.get_heuristic(start, goal), start])
    
    while len(agenda) != 0:
        path = agenda.pop(0)
        node = path[-1]

        if node == goal:
            print(agenda, end="\n\n")
            return path[1:]
                    

        neighbors = graph.get_connected_nodes(node)

        for n in neighbors:
            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)
                
                h =  graph.get_heuristic(n, goal)
                path_copy[0] = h

                agenda.append(path_copy)
                    
        agenda = sorted(agenda, key=lambda x:(x[0]))
        agenda = agenda[:beam_width]
        print(agenda,  end="\n\n")

    return []


def ucs(graph: Graph, start, goal):
    agenda = []
    agenda.append([start])
    
    while len(agenda) != 0:
        path = agenda.pop(0)
        node = path[-1]

        if node == goal:
            print(agenda, end="\n\n")
            return path
                    

        neighbors = graph.get_connected_nodes(node)

        for n in neighbors:
            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)
                agenda.append(path_copy)
                    
        agenda = sorted(agenda, key=lambda x:path_length(graph, x))
        print(agenda,  end="\n\n")

    return []

# todo: fix node priority in agenda paths
def a_star(graph: Graph, start, goal):
    agenda = []
    agenda.append([graph.get_heuristic(start, goal), start])
    print(agenda, end="\n\n")
    
    while len(agenda) != 0:


        path = agenda.pop(0)
        node = path[-1]

        if node == goal:
            print(agenda, end="\n\n")
            return path[1:]

        neighbors = graph.get_connected_nodes(node)
        
        extended_nodes = []

        for n in neighbors:

            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)

                path_length = 0
                for i in range(1, len(path_copy) - 2):
                    path_length += graph.get_edge(path_copy[i], path_copy[i + 1]).length

                h = graph.get_edge(path[-1], n).length + graph.get_heuristic(n, goal) + path_length
                
                path_copy[0] = h
                extended_nodes.append(path_copy)         

                    
        extended_nodes = extended_nodes[::-1]
        # print(extended_nodes)

        if len(agenda) == 0:
            for extended_node in extended_nodes:
                agenda.insert(0, extended_node) 
        else:
            agenda_copy = agenda.copy()
            for extended_node in extended_nodes:
                for i in range(len(agenda)):
                    path = agenda[i]

                    # heuristic comparison
                    if path[0] > extended_node[0]:
                        agenda_copy.insert(i, extended_node)
            agenda = agenda_copy
            # agenda.insert(0, extended_node)       
        
        
        # agenda = sorted(agenda, key=lambda x: (x[0], len(x)))
        # agenda = a_star_sort(agenda)

        print(agenda, end="\n\n")

    return []

# User defined functions

def a_star_sort(agenda):
    agenda_copy = agenda.copy()
    
    for i in range(len(agenda) - 1):
        for j in range(0, len(agenda) - i - 1):

            # heuristic comparison
            if agenda[j][0] > agenda[j + 1][0]:
                agenda[j], agenda[j + 1] = agenda[j + 1], agenda[j]


            elif agenda[j][0] == agenda[j + 1][0]:

                # number of visited node comparsion
                if len(agenda[j]) > len(agenda[j + 1]):
                    agenda[j], agenda[j + 1] = agenda[j + 1], agenda[j]

            
    return agenda


# (Optional) Do these for extra credit:
def is_admissible(graph, goal):
    for node in graph.nodes:
        h = graph.get_heuristic(node, goal)
        h_star = path_length(a_star(graph, node, goal))
        if not (h <= h_star):
            return False

    return True


def is_consistent(graph, goal):
    for node in graph.nodes:
        h = graph.get_heuristic(node, goal)

        neighbors = graph.get_connected_nodes(node)
        for successor in neighbors:

            c = graph.get_edge(node, successor).length
            h_successor = path_length(a_star(graph, node, goal))
            if not (h <= c + h_successor):
                return False

    return True


if __name__ == "__main__":
    # Test different graphs from 'test_data.py'
    # Be sure to change 'start' and 'goal' for each graph
    # from test_data import GRAPH1
    # graph = GRAPH1
    # start = 'The Chamber'
    # goal = 'Common Area'

    from test_data import GRAPH0
    graph = GRAPH0
    start = 'S'
    goal = 'G'
    
    # Use different algorithms here
    # path = beam_search(graph, start, goal, 1)
    path = ids(graph, start, goal)

    if path:
        print(path)

        edges = path_edges(graph, path)
        print(edges)
        cost = path_length(graph, path)
        print("Path cost=", cost)

        # Visualization (extra credit)
        try:
            # Change 'algorithm_label' for better labelling
            algorithm_label = "IDS"

            from visualize import draw_graph
            draw_graph(graph, goal=goal, output_name=algorithm_label+" Graph",
                       selected_edges=edges, graph_label=algorithm_label)
        except ModuleNotFoundError:
            print("\n\nPlease install graphviz and the python graphviz library for visualization.")
    else:
        print("Path not found")
