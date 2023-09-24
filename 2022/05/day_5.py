# Advent of Code 2022
# Day 4


"""
Crate stacks:

    [S] [C]         [Z]            
[F] [J] [P]         [T]     [N]    
[G] [H] [G] [Q]     [G]     [D]    
[V] [V] [D] [G] [F] [D]     [V]    
[R] [B] [F] [N] [N] [Q] [L] [S]    
[J] [M] [M] [P] [H] [V] [B] [B] [D]
[L] [P] [H] [D] [L] [F] [D] [J] [L]
[D] [T] [V] [M] [J] [N] [F] [M] [G]
 1   2   3   4   5   6   7   8   9 

"""
original_stacks = {}
original_stacks[1] = ['D', 'L', 'J', 'R', 'V', 'G', 'F']
original_stacks[2] = ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S']
original_stacks[3] = ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C']
original_stacks[4] = ['M', 'D', 'P', 'N', 'G', 'Q']
original_stacks[5] = ['J', 'L', 'H', 'N', 'F']
original_stacks[6] = ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z']
original_stacks[7] = ['F', 'D', 'B', 'L']
original_stacks[8] = ['M', 'J', 'B', 'S', 'V', 'D', 'N']
original_stacks[9] = ['G', 'L', 'D']


def get_procedure():
    with open("input.txt", 'r') as file:
        procedure = file.read().split('\n')
        procedure_numbers = []
        for step in procedure:
            numbers = [int(i) for i in step.split() if i.isdigit()]
            procedure_numbers.append(numbers)
        return procedure_numbers


def move_with_cargo_crane(stacks, procedure):
    for step in procedure:
        crates = step[0]
        move_from = step[1]
        move_to = step[2]
        for crate in range(crates):
            picked_up = stacks[move_from].pop()
            stacks[move_to].append(picked_up)
    return [stacks[i][-1] for i in range(1, 10)]

def move_with_crate_mover_9001(stacks, procedure):
    for step in procedure:
        crates = step[0]
        move_from = step[1]
        move_to = step[2]

        picked_up = stacks[move_from][-crates:]
        del stacks[move_from][-crates:]
        stacks[move_to].extend(picked_up)
    return [stacks[i][-1] for i in range(1, 10)]

procedure = get_procedure()

crane_stacked = move_with_cargo_crane(original_stacks, procedure)
crane_answer = "".join(crane_stacked)
crate_mover_stacked = move_with_crate_mover_9001(original_stacks, procedure)
crate_mover_answer =  "".join(crate_mover_stacked)

print(f"Top crates (Part 1): {crane_answer}")
print(f"Top crates (Part 2): {crate_mover_answer}")
