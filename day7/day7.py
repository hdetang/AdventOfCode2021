import numpy as np

def getCost(positions, expensive = False):
    cheapestCost = None
    
    for index in range(max(positions) + 1):
        cost = 0
        for position in positions:
            steps = abs(position - index)
            cost += steps if expensive == False else int(steps * (steps + 1) / 2)

        if cheapestCost == None or cost < cheapestCost:
            cheapestCost = cost
        
    return cheapestCost

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    positions = np.array(input[0].split(','))
    positions = positions.astype(int)

    print(getCost(positions))
    print(getCost(positions, True))
