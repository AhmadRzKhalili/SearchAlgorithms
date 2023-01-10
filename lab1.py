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
    
    # level = 0
    # level_limit = 0

    
    # agenda = []
    # agenda.append([start])
    
    # while len(agenda) != 0:

    #     if level <= level_limit:
    #         if level == 0:
    #             agenda = []
    #             agenda.append([start])


    #         path = agenda.pop(0)
    #         node = path[-1]

    #         if node == goal:
    #             print(agenda, end="\n\n")
    #             return path

    #         neighbors = graph.get_connected_nodes(node)

    #         extended_nodes = []

    #         for n in neighbors:

    #             if n not in path:
    #                 path_copy = path.copy()
    #                 path_copy.append(n)
    #                 extended_nodes.append(path_copy)
    #                 # agenda.insert(0, path_copy)            

                        
    #         extended_nodes = extended_nodes[::-1]
    #         for extended_node in extended_nodes:
    #             agenda.insert(0, extended_node)       
            
    #         print(agenda,  end="\n\n")

    #         level += 1

    #     if level > level_limit:
    #         # print("-", (level - 1), agenda,  end="\n\n")
    #         level = 0
    #         level_limit += 1

    return []


def hill_climbing(graph: Graph, start, goal):
    raise NotImplementedError


def beam_search(graph: Graph, start, goal, beam_width):
    raise NotImplementedError


def ucs(graph: Graph, start, goal):
    raise NotImplementedError


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

                # print(path[-1], "->", n, graph.get_edge(path[-1], n).length)
                # print(n, "->",graph.get_heuristic(n, goal))
                # print(path[-1], "->", graph.get_heuristic(path[-1], goal))

                path_length = 0
                for i in range(1, len(path_copy) - 2):
                    path_length += graph.get_edge(path_copy[i], path_copy[i + 1]).length

                h = graph.get_edge(path[-1], n).length + graph.get_heuristic(n, goal) + path_length
                # graph.set_heuristic(n, goal, h)
                
                path_copy[0] = h
                extended_nodes.append(path_copy)         

                    
        extended_nodes = extended_nodes[::-1]
        for extended_node in extended_nodes:
            agenda.insert(0, extended_node)       
        
        
        agenda = sorted(agenda, key=lambda x: (x[0], len(x)))
        # agenda.sort(key=sort_by_heuristic)

        print(agenda, end="\n\n")

    return []

def sort_by_heuristic(p):
  return p[0]

# (Optional) Do these for extra credit:
def is_admissible(graph, goal):
    raise NotImplementedError


def is_consistent(graph, goal):
    raise NotImplementedError


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
    path = a_star(graph, start, goal)

    if path:
        print(path)

        edges = path_edges(graph, path)
        print(edges)
        cost = path_length(graph, path)
        print("Path cost=", cost)

        # Visualization (extra credit)
        try:
            # Change 'algorithm_label' for better labelling
            algorithm_label = "A_star"

            from visualize import draw_graph
            draw_graph(graph, goal=goal, output_name=algorithm_label+" Graph",
                       selected_edges=edges, graph_label=algorithm_label)
        except ModuleNotFoundError:
            print("\n\nPlease install graphviz and the python graphviz library for visualization.")
    else:
        print("Path not found")
