# Advent of Code 2022
# Day 12

from collections import namedtuple

Node = namedtuple("Node", ["x", "y", "z"])
node_count = 0
nodes = {}
starting_nodes = []

with open("input2.txt") as f:
    lines = f.read().splitlines()
for ycoord, line in enumerate(lines):
    for xcoord, char in enumerate(line):
        nodes[node_count] = Node(xcoord, ycoord, ord(char))
        if ord(char) == 69:
            destination_node = node_count
            nodes[node_count] = Node(xcoord, ycoord, 122)
        if ord(char) == 83 or ord(char) == 97:
            starting_nodes.append(node_count)
            nodes[node_count] = Node(xcoord, ycoord, 97)
        node_count += 1

shortest_paths = {}
for node in starting_nodes:
    shortest_paths[node] = {key: float('inf') for key in nodes}

for node in starting_nodes:
    shortest_paths[node][node] = 0

previous_node = {node: None for node in nodes}
unvisited = [node for node in nodes]

# Set the height and shortest distance of the starting position
while destination_node in unvisited:
    # find the node witht the shortest distance from S:
    current_key = min(unvisited, key = lambda node: shortest_path[node])
    current_node = nodes[current_key]
    # each node key of unvisited will be passed as an arg to shortest path. the smallest will
    # be found and the key for smallest is returned from unvisited

    # Finding unvisited reachable nieghbours:
    neighbours = []
    for key, node in nodes.items():
        if key in unvisited:
            if key != current_key:
                if node.z <= current_node.z +1:
                    if ((node.y == current_node.y and 
                    node.x in range(current_node.x - 1, current_node.x + 2)) or 
                    (node.x == current_node.x and 
                    node.y in range(current_node.y - 1, current_node.y + 2))):
                        neighbours.append(key)
    for neighbour in neighbours:
        # if distance from S to current node +
        # current node to neighbour  < known distance:
        if shortest_path[current_key] + 1 <= shortest_path[neighbour]:
            shortest_path[neighbour] = shortest_path[current_key] + 1
            previous_node[neighbour] = current_node
    unvisited.remove(current_key)


print(f"shortest path to dest node: {shortest_path[destination_node]}")
print(f"previous = {previous_node[destination_node]}")
print(nodes[destination_node])