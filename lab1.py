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
        neighbors = graph.get_connected_nodes(node)

        for n in neighbors:
            if n not in path:
                path_copy = path.copy()
                path_copy.append(n)
                agenda.append(path_copy)

                if n == goal:
                    print(agenda, end="\n\n")
                    return path_copy
                    
                    
        
        print(agenda,  end="\n\n")

    return []




def dfs(graph: Graph, start, goal):
    raise NotImplementedError


def ids(graph: Graph, start, goal):
    raise NotImplementedError


def hill_climbing(graph: Graph, start, goal):
    raise NotImplementedError


def beam_search(graph: Graph, start, goal, beam_width):
    raise NotImplementedError


def ucs(graph: Graph, start, goal):
    raise NotImplementedError


def a_star(graph: Graph, start, goal):
    raise NotImplementedError


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

    from test_data import TESTGRAPH
    graph = TESTGRAPH
    start = 'S'
    goal = 'G'

    # Use different algorithms here
    path = bfs(graph, start, goal)

    if path:
        edges = path_edges(graph, path)
        print(edges)
        cost = path_length(graph, path)
        print("Path cost=", cost)

        # Visualization (extra credit)
        try:
            # Change 'algorithm_label' for better labelling
            algorithm_label = "BFS"

            from visualize import draw_graph
            draw_graph(graph, goal=goal, output_name=algorithm_label+" Graph",
                       selected_edges=edges, graph_label=algorithm_label)
        except ModuleNotFoundError:
            print("\n\nPlease install graphviz and the python graphviz library for visualization.")
    else:
        print("Path not found")
