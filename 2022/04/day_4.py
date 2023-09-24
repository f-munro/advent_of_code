# Advent of Code 2022
# Day 4

# Get the assignments as a list of tuple pairs
def get_assignments():
    with open("/Volumes/Macintosh HD/Code/AdventOfCode/2022/input_4.txt", 'r') as file:
        assignments = file.read().split('\n')
        assignment_tuples = []
        for line in assignments:
            pair = line.split(",")
            tup = (pair[0], pair[1])
            assignment_tuples.append(tup)
        return assignment_tuples  

# Check a pair for any full overlaps
def check_full_overlap(assignment):
    x = assignment[0].split(",")
    y = x[0].split("-")
    x2 = assignment[1].split(",")
    z = y + x2[0].split("-")
    if int(z[0]) <= int(z[2]) and int(z[1]) >= int(z[3]):
        return True
    elif int(z[2]) <= int(z[0]) and int(z[3]) >= int(z[1]):
        return True
    else:
        return False

# Check a pair for any partial overlaps
def check_partial_overlap(assignment):
    x = assignment[0].split(",")
    y = x[0].split("-")
    x2 = assignment[1].split(",")
    z = y + x2[0].split("-")
    for i in range(int(z[0]), (int(z[1])+1)):
        if i in range(int(z[2]),int(z[3])+1):
            return True


assignments = get_assignments()

count = 0
partial_count = 0
for i in assignments:
    result = check_full_overlap(i)
    if result is True:
        count += 1
    partial_overlap = check_partial_overlap(i)
    if partial_overlap is True:
        partial_count += 1

print(f"Total: {count}")
print(f"Total partial overlaps: {partial_count}")