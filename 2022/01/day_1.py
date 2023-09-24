# Advent of Code 2022
# Day 1

def elf_calorie_totals():
    with open("/Volumes/Macintosh HD/Code/AdventOfCode/2022/input_1.txt", 'r') as file:
        elves = file.read().split('\n\n')

        calorie_totals = []
        for elf in elves:
            item_calories = elf.split('\n')
            item_calories = [int(item) for item in item_calories]
            total_calories = sum(item_calories)
            calorie_totals.append(total_calories)
        return calorie_totals


    
result = elf_calorie_totals()
result.sort(reverse=True)

top_3_total = 0
for total in result[:3]:
    top_3_total += total

print("Largest is:", max(result))
print(f"Largest 3 are: {top_3_total}")
