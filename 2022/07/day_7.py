# Advent of Code 2022
# Day 7
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) 
input_file_path = os.path.join(script_dir, "input.txt")

def get_filesystem(needed):
    with open(input_file_path, 'r') as file:
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

        input = file.read().split('\n')
        for line in input:
            if line.startswith("$ cd"):
                dir = line[5:]
                if dir.isalpha():
                    # going down a level
                    dir_lvl += 1
                elif dir == "..":
                    # Going back up a level means we can check the total
                    # filesize of the level, add it to the total sum if
                    # needed, and reset the level to 0.
                    if dir_totals[dir_lvl] <= 100_000:
                        total_sum += dir_totals[dir_lvl]
                    # need to compare it with 'space required' to find
                    # the directory we should delete.
                    #check_directory(8381165, dir_totals[dir_lvl])
                    if dir_totals[dir_lvl] > needed:
                        difference = dir_totals[dir_lvl] - needed
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
        "total_sum": total_sum,
        "total_disk_size": dir_totals[1],
        "space needed": space_needed,
        "smallest dir": smallest_dir_size
    }
    return answers


ans = get_filesystem(389918)

update = 30_000_000
free_space = (70_000_000 - ans["total_disk_size"])
space_needed = update - free_space

print(f"free space:{free_space}")
print(f"space required:{space_needed}")
print(f"smallest directory :{ans['smallest dir']}")