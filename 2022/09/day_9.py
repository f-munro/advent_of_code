# Advent of Code 2022
# Day 9


def move(head_pos, tail_pos, direction, steps):
    global map
    global spaces_visited

    new_head_pos = {"x": head_pos["x"], "y": head_pos["y"]}

    # mark new tail positions on the map:
    if map[tail_pos['x']][tail_pos["y"]] == 0:
        map[tail_pos['x']][tail_pos["y"]] = 1
        spaces_visited +=1

    # run the function recursively for the number of steps:
    if steps == 0:
         return new_head_pos, tail_pos
    
    if direction == "U":
        new_head_pos["x"] -= 1
    if direction == "D":
        new_head_pos["x"] += 1
    if direction == "L":
        new_head_pos["y"] -= 1
    if direction == "R":
        new_head_pos["y"] += 1

    if (abs(new_head_pos["x"] - tail_pos["x"]) > 1 or 
        abs(new_head_pos["y"] - tail_pos["y"]) > 1):
            tail_pos = {"x": head_pos["x"], "y": head_pos["y"]}

    return move(new_head_pos, tail_pos, direction, steps -1)


# make a big map
map = []
for i in range(500):
    row = []
    for j in range(500):
        row.append(0)
    map.append(row)

# keep track of the number of new
# spaces visited by the tail
spaces_visited = 0

# start the rope somewhere in the middle of the map
head_pos = {"x": 200, "y": 200}
tail_pos = {"x": 200, "y": 200}


with open("input.txt") as f:
    lines = f.read().splitlines()


for line in lines:
    movement = line.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    head_pos, tail_pos = move(head_pos, tail_pos, direction, steps)


print(f"Spaces visited: {spaces_visited}")
