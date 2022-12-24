from os import path
import graphviz


def draw_graph(graph, goal=None, selected_edges=[], output_dir="output", output_name="graph-output", graph_label="Graph"):
    dot = graphviz.Graph(format="png")
    selected_nodes = set([e.node1 for e in selected_edges] +
                         [e.node2 for e in selected_edges])
    dot.attr(label=graph_label)
    [dot.node(x, shape="circle") if not goal else
        (
            dot.node(x, shape="circle", color="red", xlabel=str(graph.get_heuristic(x, goal))) if x != goal else
        dot.node(x, xlabel='0', color="red", shape="doublecircle")
    ) if x in selected_nodes else
        dot.node(x, shape="circle", xlabel=str(graph.get_heuristic(x, goal))) if x != goal else
        dot.node(x, xlabel='0', shape="doublecircle")
        for x in graph.nodes]
    [dot.edge(x.node1, x.node2, str(x.length), fontcolor="darkgreen")
     if x not in selected_edges
     else dot.edge(x.node1, x.node2, str(x.length), color="red", fontcolor="darkgreen")
     for x in graph.edges]
    dot.render(path.join(output_dir, output_name))


if __name__ == "__main__":
    from test_data import TESTGRAPH
    draw_graph(TESTGRAPH)
