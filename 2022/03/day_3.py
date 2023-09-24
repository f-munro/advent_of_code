# Advent of Code 2022
# Day 3


# Making a dictionary of letters and their numerical values
# a-z = 1-26    A-Z = 27-52
letters = {chr(i + 96): i for i in range(1, 27)}
letters_2 = {chr(i + 38): i for i in range(27, 53)}
letters.update(letters_2)

def get_rucksacks():
       with open("input.txt", 'r') as file:
            # Get all the rucksacks:
            rucksacks = file.read().split('\n')
            return rucksacks

     
def get_badges(rucksacks):
    badges = []
    length = len(rucksacks)

    # Group rucksacks into groups of three:
    j = 3
    for i in range(0, length, 3):
        # Find the item that appears in all three
        # to find the item that corresponds to the badge
        group = rucksacks[i:j]
        for item in group[0]:
            if item in group[1] and item in group[2]:
                  # Convert the badge into its priority number:
                  badges.append(letters[item])
                  break
        j += 3 
    return badges
      

def get_duplicates(rucksacks):
            duplicates = []
            for rucksack in rucksacks:
                size = len(rucksack)
                # Get each compartment:
                compartment_1 = rucksack[:(size//2)]
                compartment_2 = rucksack[(size//2):size]
                # Find the item type that appears in both compartments
                # and add them as their priority number to a list
                for item in compartment_1:
                     if item in compartment_2:
                          duplicates.append(letters[item])
                          break
            return duplicates
                 

rucksacks = get_rucksacks()
duplicates = get_duplicates(rucksacks)
badges = get_badges(rucksacks)

print(f"Total of duplicate items: {sum(duplicates)}")
print(f"Total of badges: {sum(badges)}")