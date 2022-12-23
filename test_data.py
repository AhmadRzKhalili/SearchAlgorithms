# Fall 2012 6.034 Lab 2: Search

from graph import Edge, Graph, NODE1, NODE2, VAL

# The graphs you will use for the problem set.

# The heuristic values
# are lower bounds on the distance to the node with the id of
## "Common Area"

GRAPH0 = Graph(edges=[Edge.fromdict(e) for e in [{VAL: 1, NODE1: 'S', NODE2: 'A'},
                                                 {VAL: 1, NODE1: 'S', NODE2: 'B'},
                                                 {VAL: 1, NODE1: 'A', NODE2: 'C'},
                                                 {VAL: 1, NODE1: 'A', NODE2: 'D'},
                                                 {VAL: 1, NODE1: 'B', NODE2: 'D'},
                                                 {VAL: 1, NODE1: 'B', NODE2: 'G'},
                                                 {VAL: 1, NODE1: 'c', NODE2: 'D'},
                                                 {VAL: 1, NODE1: 'D', NODE2: 'G'},
                                                 ]],
               heuristic={'G':
               {'S': 17,
                'A': 10,
                'B': 7,
                'C': 13,
                'D': 15}})

GRAPH1 = Graph(edges=[Edge.fromdict(e) for e in [{VAL: 5, NODE1: 'Common Area', NODE2: 'Stairs'},
                                                 {VAL: 15, NODE1: 'Entrance Hall',
                                                  NODE2: 'Hospital'},
                                                 {VAL: 7, NODE1: 'Classroom 11',
                                                  NODE2: 'Hospital'},
                                                 {VAL: 25, NODE1: 'Haunted Bathroom',
                                                  NODE2: 'The Chamber'},
                                                 {VAL: 5, NODE1: 'Forbidden Area',
                                                  NODE2: 'Trophy Room'},
                                                 {VAL: 3, NODE1: 'Mirrored Room',
                                                  NODE2: 'Statues'},
                                                 {VAL: 1, NODE1: 'Grand Hall',
                                                  NODE2: 'Entrance Hall'},
                                                 {VAL: 4, NODE1: 'Dungeon 5',
                                                  NODE2: 'Haunted Bathroom'},
                                                 {VAL: 2, NODE1: 'Stairs',
                                                  NODE2: 'Grand Hall'},
                                                 {VAL: 9, NODE1: 'Statues',
                                                  NODE2: 'Stairs'},
                                                 {VAL: 6, NODE1: 'Entrance Hall',
                                                  NODE2: 'Haunted Bathroom'},
                                                 {VAL: 4, NODE1: 'Forbidden Area',
                                                  NODE2: 'Stairs'},
                                                 {VAL: 10, NODE1: 'Classroom 11',
                                                  NODE2: 'Entrance Hall'},
                                                 {VAL: 5, NODE1: 'Trophy Room',
                                                  NODE2: 'Stairs'},
                                                 {VAL: 8, NODE1: 'Stairs',
                                                  NODE2: 'Mirrored Room'},
                                                 {VAL: 3, NODE1: 'Entrance Hall',
                                                  NODE2: 'Stairs'},
                                                 {VAL: 8, NODE1: 'Necessary Room',
                                                  NODE2: 'Common Area'}
                                                 ]],
               heuristic={'Common Area':
               {'Hospital': 17,
                'Classroom 11': 10,
                'Entrance Hall': 7,
                'Haunted Bathroom': 13,
                'Dungeon 5': 15,
                'The Chamber': 14,
                'Forbidden Area': 8,
                'Trophy Room': 6,
                'Stairs': 4,
                'Grand Hall': 6,
                'Common Area': 0,
                'Statues': 12,
                'Mirrored Room': 10,
                'Necessary Room': 6}})

GRAPH2 = Graph(edges=[Edge.fromdict(e) for e in [
    {VAL: 10, NODE1: 'S', NODE2: 'A'},
    {VAL: 4, NODE1: 'S', NODE2: 'B'},
    {VAL: 9, NODE1: 'A', NODE2: 'C'},
    {VAL: 8, NODE1: 'B', NODE2: 'C'},
    {VAL: 7, NODE1: 'C', NODE2: 'D'},
    {VAL: 9, NODE1: 'C', NODE2: 'E'},
    {VAL: 7, NODE1: 'D', NODE2: 'E'},
    {VAL: 13, NODE1: 'D', NODE2: 'F'},
    {VAL: 8, NODE1: 'E', NODE2: 'F'},
    {VAL: 5, NODE1: 'E', NODE2: 'G'},
    {VAL: 10, NODE1: 'F', NODE2: 'G'}]],
    heuristic={'G': {'S': 25, 'A': 20, 'B': 22, 'C': 15, 'D': 8, 'E': 3, 'F': 9}})

GRAPH3 = Graph(edges=[Edge.fromdict(e) for e in [
    {VAL: 6, NODE1: 'S', NODE2: 'B'},
    {VAL: 10, NODE1: 'S', NODE2: 'A'},
    {VAL: 10, NODE1: 'A', NODE2: 'B'},
    {VAL: 7, NODE1: 'B', NODE2: 'C'},
    {VAL: 4, NODE1: 'A', NODE2: 'D'},
    {VAL: 2, NODE1: 'C', NODE2: 'D'},
    {VAL: 6, NODE1: 'C', NODE2: 'G'},
    {VAL: 8, NODE1: 'G', NODE2: 'D'}]],
    heuristic={'G': {"S": 0, "A": 2, "B": 5, "C": 6, "D": 5}})

GRAPH4 = Graph(edges=[Edge.fromdict(e) for e in [
    {VAL: 1, NODE1: 'S', NODE2: 'A'},
    {VAL: 1, NODE1: 'S', NODE2: 'B'},
    {VAL: 1, NODE1: 'A', NODE2: 'B'},
    {VAL: 1, NODE1: 'C', NODE2: 'A'},
    {VAL: 1, NODE1: 'C', NODE2: 'B'},
    {VAL: 1, NODE1: 'D', NODE2: 'C'},
    {VAL: 1, NODE1: 'D', NODE2: 'B'},
    {VAL: 1, NODE1: 'E', NODE2: 'C'},
    {VAL: 1, NODE1: 'E', NODE2: 'D'},
    {VAL: 1, NODE1: 'F', NODE2: 'D'},
    {VAL: 1, NODE1: 'F', NODE2: 'E'},
    {VAL: 1, NODE1: 'G', NODE2: 'E'},
    {VAL: 1, NODE1: 'G', NODE2: 'F'}]],
    heuristic={"G": {"S": 1, "A": 3, "B": 3, "C": 2, "D": 2, "E": 1, "F": 1}})

GRAPH5 = Graph(edges=[Edge.fromdict(e) for e in [
    {VAL:  1, NODE1: 'S', NODE2: 'A'},
    {VAL:  1, NODE1: 'G', NODE2: 'C'},
    {VAL: 100, NODE1: 'B', NODE2: 'C'},
    {VAL: 10, NODE1: 'S', NODE2: 'B'},
    {VAL: 10, NODE1: 'C', NODE2: 'A'}]],
    heuristic={"G": {"S": 10, "A": 1000, "B": 5, "C": 5}})

SAQG = Graph(edges=[Edge.fromdict(e) for e in [
    {'LENGTH': 1, 'NODE1': 'S', 'NODE2': 'A'},
    {'LENGTH': 1, 'NODE1': 'S', 'NODE2': 'Q'},
    {'LENGTH': 1, 'NODE1': 'A', 'NODE2': 'G'},
    {'LENGTH': 1, 'NODE1': 'Q', 'NODE2': 'G'},
    {'LENGTH': 1, 'NODE1': 'S', 'NODE2': 'G'}]])

NEWGRAPH1 = Graph(edges=[Edge.fromdict(e) for e in [
    {'LENGTH':  6, 'NODE1': 'S', 'NODE2': 'A'},
    {'LENGTH':  4, 'NODE1': 'A', 'NODE2': 'B'},
    {'LENGTH':  7, 'NODE1': 'B', 'NODE2': 'F'},
    {'LENGTH':  6, 'NODE1': 'C', 'NODE2': 'D'},
    {'LENGTH':  3, 'NODE1': 'C', 'NODE2': 'A'},
    {'LENGTH':  7, 'NODE1': 'E', 'NODE2': 'D'},
    {'LENGTH':  6, 'NODE1': 'D', 'NODE2': 'H'},
    {'LENGTH':  2, 'NODE1': 'S', 'NODE2': 'C'},
    {'LENGTH':  2, 'NODE1': 'B', 'NODE2': 'D'},
    {'LENGTH': 25, 'NODE1': 'E', 'NODE2': 'G'},
    {'LENGTH':  5, 'NODE1': 'E', 'NODE2': 'C'}]],
    heuristic={"G": {'S': 11,
                     'A': 9,
                     'B': 6,
                     'C': 12,
                     'D': 8,
                     'E': 15,
                     'F': 1,
                     'H': 2},
               "H": {'S': 11,
                     'A': 9,
                     'B': 6,
                     'D': 12,
                     'E': 8,
                     'F': 15,
                     'G': 14},
               'A': {'S': 5,  # admissible
                     # h(d) > h(b)+c(d->b) ...  6 > 1 + 2
                     "B": 1,
                     "C": 3,
                     "D": 6,
                     "E": 8,
                     "F": 11,
                     "G": 33,
                     "H": 12},
               'C': {"S": 2,  # consistent
                     "A": 3,
                     "B": 7,
                     "D": 6,
                     "E": 5,
                     "F": 14,
                     "G": 30,
                     "H": 12},
               "D": {"D": 3},  # dumb
               "E": {}  # empty
               })

NEWGRAPH2 = Graph(edges=[Edge.fromdict(e) for e in [{'LENGTH': 2, 'NODE1': 'D', 'NODE2': 'F'},
                         {'LENGTH': 4,
                          'NODE1': 'C', 'NODE2': 'E'},
                         {'LENGTH': 2,
                          'NODE1': 'S', 'NODE2': 'B'},
                         {'LENGTH': 5,
                          'NODE1': 'S', 'NODE2': 'C'},
                         {'LENGTH': 4,
                          'NODE1': 'S', 'NODE2': 'A'},
                         {'LENGTH': 8,
                          'NODE1': 'F', 'NODE2': 'G'},
                         {'LENGTH': 5,
                          'NODE1': 'D', 'NODE2': 'C'},
                         {'LENGTH': 6, 'NODE1': 'D', 'NODE2': 'H'}]],
                  heuristic={"G": {'S': 9,
                                   'A': 1,
                                   'B': 2,
                                   'C': 3,
                                   'D': 6,
                                   'E': 5,
                                   'F': 15,
                                   'H': 10}})


NEWGRAPH3 = Graph(nodes=["S"])


NEWGRAPH4 = Graph(nodes=["S", "A", "B", "C", "D", "E", "F", "H", "J", "K",
                         "L", "T"],
                  edges=[Edge.fromdict(e) for e in [{'LENGTH': 2, 'NODE1': 'S', 'NODE2': 'A'},
                         {'LENGTH': 10,
                          'NODE1': 'S', 'NODE2': 'B'},
                         {'LENGTH': 5,
                          'NODE1': 'B', 'NODE2': 'C'},
                         {'LENGTH': 2,
                          'NODE1': 'B', 'NODE2': 'F'},
                         {'LENGTH': 5,
                          'NODE1': 'C', 'NODE2': 'E'},
                         {'LENGTH': 12,
                          'NODE1': 'C', 'NODE2': 'J'},
                         {'LENGTH': 8,
                          'NODE1': 'F', 'NODE2': 'H'},
                         {'LENGTH': 3,
                          'NODE1': 'H', 'NODE2': 'D'},
                         {'LENGTH': 5,
                          'NODE1': 'H', 'NODE2': 'K'},
                         {'LENGTH': 1,
                          'NODE1': 'K', 'NODE2': 'J'},
                         {'LENGTH': 4,
                          'NODE1': 'J', 'NODE2': 'L'},
                         {'LENGTH': 7,
                          'NODE1': 'K', 'NODE2': 'T'},
                         {'LENGTH': 5,
                          'NODE1': 'L', 'NODE2': 'T'},
                         ]],
                  heuristic={"T": {'S': 10,
                                   'A': 6,
                                   'B': 5,
                                   'C': 2,
                                   'D': 5,
                                   'E': 1,
                                   'F': 100,
                                   'H': 2,
                                   'J': 3,
                                   'K': 100,
                                   'L': 4,
                                   'T': 0, }})


# the heuristic is admissible but not consistent,
AGRAPH = Graph(nodes=['S', 'A', 'B', 'C', 'G'],
               edges=[Edge.fromdict(e) for e in [{'LENGTH': 3, 'NODE1': 'S', 'NODE2': 'A'},
                      {'LENGTH': 1,
                       'NODE1': 'S', 'NODE2': 'B'},
                      {'LENGTH': 1,
                       'NODE1': 'A', 'NODE2': 'B'},
                      {'LENGTH': 1,
                       'NODE1': 'A', 'NODE2': 'C'},
                      {'LENGTH': 10, 'NODE1': 'C', 'NODE2': 'G'}]],
               heuristic={'G': {'S': 12,
                                'A': 9,
                                'B': 12,
                                'C': 8,
                                'G': 0}})
