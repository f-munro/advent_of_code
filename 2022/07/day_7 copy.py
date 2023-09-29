# Advent of Code 2022
# Day 7



with open("input.txt", 'r') as file:
    input = file.read().split('\n')

def check_filesystem(space_needed):
    # Keep track of the current directory level 
    dir_lvl = 1

    # Create a dictionary of keys for each level
    dir_totals = {key:0 for key in range(1, 20)}

    # For part 1, all directories with a size <= 100,000
    # will be added to the total sum 
    total_sum = 0

    # for part 2:
    smallest_difference = 100_000_000
    smallest_dir_size = 0

    for line in input:
        if line.startswith("$ cd"):
            dir = line[5:]
            if dir.isalpha():
                # going down a level
                dir_lvl += 1
            elif dir == "..":
                # Going back up a level means the total size of
                # dir can be checked, and added to the total sum
                # if small enough, and the level reset to 0.
                if dir_totals[dir_lvl] <= 100_000:
                    total_sum += dir_totals[dir_lvl]
                # need to compare it with 'space required' to find
                # the directory we should delete.
                if dir_totals[dir_lvl] > space_needed:
                    difference = dir_totals[dir_lvl] - space_needed
                    if difference < smallest_difference:
                        smallest_difference = difference
                        smallest_dir_size = dir_totals[dir_lvl]

                dir_totals[dir_lvl] = 0
                dir_lvl -= 1

        elif line[0].isdecimal():
            file = line.split(" ")
            filesize = file[0]
            for i in range(dir_lvl, 0, -1):
                dir_totals[i] += int(filesize)

    # For part 2:
    update_size = 30_000_000
    free_space = (70_000_000 - dir_totals[1])
    space_needed = update_size - free_space
    
    answers = {
        "sum of directories": total_sum,
        "space used": dir_totals[1],
        "space needed": space_needed,
        "smallest directory": smallest_dir_size
    }
    return answers


ans = check_filesystem(389918)

update = 30_000_000
free_space = (70_000_000 - ans["space used"])
space_needed = update - free_space

print(f"free space:{free_space}")
print(f"space required:{space_needed}")
print(f"smallest directory :{ans['smallest directory']}")