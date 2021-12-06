import numpy as np

def calculateSchool(fishes, days):
    oldFishes = {}
    youngFishes = {}

    maxNewFish = 8
    maxOldFish = 6

    for fish in fishes:
        if fish not in oldFishes:
            oldFishes[fish] = 1
            continue
        oldFishes[fish] += 1

    for day in range(days):
        newOldFishes = {}
        newYoungFishes = {}

        for index, school in oldFishes.items():
            newIndex = index - 1 if index > 0 else maxOldFish

            newOldFishes[newIndex] = school

            if newIndex == maxOldFish:
                newYoungFishes[maxNewFish] = school

        for index, school in youngFishes.items():
            newIndex = index - 1 if index > 0 else maxNewFish
            
            existingFishes = newYoungFishes[newIndex] if newIndex in newYoungFishes else 0
            newYoungFishes[newIndex] = existingFishes + school

            if newIndex == maxNewFish:
                newOldFishes[maxOldFish] = newOldFishes[maxOldFish] + school if maxOldFish in newOldFishes else school
    
        oldFishes = newOldFishes
        youngFishes = newYoungFishes

    return sum(oldFishes.values()) + sum(youngFishes.values())

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    fishes = np.array(input[0].split(','))
    fishes = fishes.astype(int)

    print(calculateSchool(fishes, 80))
    print(calculateSchool(fishes, 256))