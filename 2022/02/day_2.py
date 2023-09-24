# Advent of Code 2022
# Day 2

# Part 1:
# A X = 1 Rock
# B Y = 2 Paper
# C Z = 3 Scissors

# Part 2:
# X Lose
# Y Draw
# Z Win

def get_guide():
    with open("/Volumes/Macintosh HD/Code/AdventOfCode/2022/input_2.txt", 'r') as file:
        strategy_guide = file.read().split('\n')
        list = []
        for round in strategy_guide:
            list.append((round[0], round[2]))
        return list

def score_round(round):
    if round[0] == "A":
        if round[1] == "X":
            result = 3
            shape_score = 1
        elif round[1] == "Y":
            result = 6
            shape_score = 2
        else:
            result = 0
            shape_score = 3
        return result + shape_score
    if round[0] == "B":
        if round[1] == "X":
            result = 0
            shape_score = 1
        elif round[1] == "Y":
            result = 3
            shape_score = 2
        else:
            result = 6
            shape_score = 3
        return result + shape_score
    if round[0] == "C":
        if round[1] == "X":
            result = 6
            shape_score = 1
        elif round[1] == "Y":
            result = 0
            shape_score = 2
        else:
            result = 3
            shape_score = 3
        return result + shape_score


def score_round_variant(round):
    if round[0] == "A":
        if round[1] == "X":
            round_score = 0
            shape_score = 3
        elif round[1] == "Y":
            round_score = 3
            shape_score = 1
        else:
            round_score = 6
            shape_score = 2
    if round[0] == "B":
        if round[1] == "X":
            round_score = 0
            shape_score = 1
        elif round[1] == "Y":
            round_score = 3
            shape_score = 2
        else:
            round_score = 6
            shape_score = 3
    if round[0] == "C":
        if round[1] == "X":
            round_score = 0
            shape_score = 2
        elif round[1] == "Y":
            round_score = 3
            shape_score = 3
        else:
            round_score = 6
            shape_score = 1
    return round_score + shape_score

guide = get_guide()
scores = []
scores_v2 = []

for round in guide:
    score = score_round(round)
    scores.append(score)
    score_v2 = score_round_variant(round)
    scores_v2.append(score_v2)

print(f"Total score (Part 1): {sum(scores)}")
print(f"Total score (Part 2): {sum(scores_v2)}")