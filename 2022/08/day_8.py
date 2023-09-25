# Advent Of Code 2022
# Day 8

with open("input.txt") as f:
    lines = f.read().splitlines()
    tree_map = []
    column_count = len(lines[0])
    row_count = len(lines)
    # make a map of all trees
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        tree_map.append(row)


def check_visibility(height, x, y):
    # start with visible being true:
    left = True
    right = True
    up = True
    down = True

    left_score = 0
    right_score = 0
    up_score = 0
    down_score = 0

    # check visibility from tree across to left edge
    for b in range(y-1, -1, -1):
        if tree_map[x][b] >= height:
            left_score += 1
            left = False
            break
        left_score += 1

    # check from tree across to right edge
    for b in range(y + 1, column_count):
        if tree_map[x][b] >= height:
            right_score += 1
            right = False
            break
        right_score +=1

    # check from tree up to the top
    for b in range(x-1, -1, -1):
        if tree_map[b][y] >= height:
            up_score += 1
            up = False
            break
        up_score += 1

    # check from tree down to bottom
    for b in range(x + 1, row_count):
        if tree_map[b][y] >= height:
            down_score += 1
            down = False
            break
        down_score += 1

    # calculate the scenic score
    scenic_score = left_score * right_score * up_score * down_score    
    
    if left or right or up or down:
        # the tree is visible from at least one side
        return {
            "visibility": 1,
            "scenic score": scenic_score
        }
    
    # otherwise, the tree is not visible
    return {
        "visibility": 0,
        "scenic score": scenic_score
    }




# Checking tree visibility and scenic score

# first, add all the visible edge trees
# which all have a scenic score of 0
visible_tree_count = (row_count * 4) - 4
highest_scenic_score = 0

# then, each tree on the map is checked
for x in range(1, row_count - 1):
    for y in range(1, column_count - 1):
        height = tree_map[x][y]
        tree_result = check_visibility(height, x, y)
        visible_tree_count += tree_result["visibility"]
        if tree_result["scenic score"] > highest_scenic_score:
            highest_scenic_score = tree_result["scenic score"]


print(f"Number of visible trees: {visible_tree_count}")
print(f"Highest scenic score: {highest_scenic_score}")
