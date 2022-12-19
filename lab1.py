from typing import List
from graph import Edge, Graph


def path_edges(graph: Graph, path) -> List[Edge]:
    # Find edges on the path
    raise NotImplementedError


def path_length(graph, path) -> int:
    # Calculate the length of the path
    raise NotImplementedError


# Implement the following algorithms:


def bfs(graph: Graph, start, goal):
    raise NotImplementedError


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
    from test_data import GRAPH1
    graph = GRAPH1
    start = 'The Chamber'
    goal = 'Common Area'

    # Use different algorithms here
    path = bfs(graph, start, goal)

    if path:
        edges = path_edges(graph, path)
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
            print(
                "\n\nPlease install graphviz and the python graphviz library for visualization.")
    else:
        print("Path not found")
