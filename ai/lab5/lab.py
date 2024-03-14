# Name: Daim Bin Khalid
# Roll NO.: 251686775

from graph import Graph


def hill_climbing(graph, start_node, goal_node):
    """
    Intro. To AI

    Lab: Hill Climb Algorithm


    In this lab you'll be implementing a Hill Climb algorithm on a very simple Graph.

    Hill climb is a heurisitc search used for mathematical optimization problems in the field of Artificial Intelligence. Given a large set
    of inputs and a good heuristic function, it tried to find a sufficiently
    good solution to the problem. This solution may not be the global maximum.

    In this lab you'll be implementing a basic version of the algorithm on
    a graph. For representing a Graph you may modify the class in the
    graph.py file accordingly. Or make your own graph as required.

    In this task you will create a function named hill_climb_search() that
    will take in the graph along with the start and the goal node. The
    function will print the path it took after reaching the goal node.

    The graph that you will work on is as follows, where the representation
    includes the node and the heuristic of that (node, heuristic):

    # A is the root node with B, C, D as successors
    (A,3) -> (B, 4), (C, 6), (D, 5)
    (B,4) -> (E, 3), (F, 2)
    (C,6) -> (G, 7), (H, 8)
    (D,5) -> (I, 6), (J, 7)
    (H,8) -> (K, 9)

    Solution: A -> C -> H -> K

    Initial node to start is "A" and the goal node is "K"
    """
    path = []
    current_node = start_node
    path.append(start_node)

    max_node = start_node

    while current_node != goal_node:
        current_h = graph.get_h(current_node)

        neighbours = graph.neighbours(current_node)
        max_node = max(neighbours, key=lambda node: graph.get_h(node))

        if graph.get_h(max_node) <= current_h:
            continue
        else:
            current_node = max_node
            path.append(current_node)

    print(f"Path: {str(path)[1:-1]}")


if __name__ == "__main__":
    graph = Graph()

    graph.edges = {'A': set(['B', 'C', 'D']),
                   'B': set(['E', 'F']),
                   'C': set(['G', 'H']),
                   'D': set(['I', 'J']),
                   'H': set(['K']),
                   'K': set([])
                   }

    graph.heuristics = {'A': 3,
                        'B': 4,
                        'C': 6,
                        'D': 5,
                        'E': 3,
                        'F': 2,
                        'G': 7,
                        'H': 8,
                        'I': 6,
                        'J': 7,
                        'K': 9
                        }

    hill_climbing(graph, 'A', 'K')
