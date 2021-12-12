def getNeighbors(xPosition, yPosition, grid):
    neighbors = []
    xShape = len(grid[0]) - 1
    yShape = len(grid) - 1

    if xPosition+1 <= xShape:
        neighbors.append([yPosition, xPosition+1])

    if xPosition-1 >= 0:
        neighbors.append([yPosition, xPosition-1])

    if yPosition+1 <= yShape:
        neighbors.append([yPosition+1, xPosition])

    if yPosition-1 >= 0:
        neighbors.append([yPosition-1, xPosition])

    if xPosition+1 <= xShape and yPosition+1 <= yShape:
        neighbors.append([yPosition+1, xPosition+1])

    if xPosition+1 <= xShape and yPosition-1 >= 0:
        neighbors.append([yPosition-1, xPosition+1])

    if xPosition-1 >= 0 and yPosition+1 <= yShape:
        neighbors.append([yPosition+1, xPosition-1])

    if xPosition-1 >= 0 and yPosition-1 >= 0:
        neighbors.append([yPosition-1, xPosition-1])

    return neighbors

def makeFlash(xPosition, yPosition, grid):
    grid[yPosition][xPosition] = grid[yPosition][xPosition] + 1

    if grid[yPosition][xPosition] != 10: return grid
    
    neighbors = getNeighbors(xPosition, yPosition, grid)

    for neighbor in neighbors:
        y, x = neighbor
        grid = makeFlash(x, y, grid)

    return grid

def step1(octopusGrid, steps):
    flashes = 0

    for _ in range(steps):
        for yIndex, octopuses in enumerate(octopusGrid):
            for xIndex, octopus in enumerate(octopuses):
                octopusGrid = makeFlash(xIndex, yIndex, octopusGrid)                

        for yIndex, octopuses in enumerate(octopusGrid):
            for xIndex, octopus in enumerate(octopuses):
                if octopus > 9:
                    octopusGrid[yIndex][xIndex] = 0
                    flashes += 1

    return flashes

def step2(octopusGrid):
    step = 1
    octopusCount = len(octopusGrid[0]) * len(octopusGrid)

    while True:
        flashes = 0

        for yIndex, octopuses in enumerate(octopusGrid):
            for xIndex, octopus in enumerate(octopuses):
                octopusGrid = makeFlash(xIndex, yIndex, octopusGrid)                

        for yIndex, octopuses in enumerate(octopusGrid):
            for xIndex, octopus in enumerate(octopuses):
                if octopus > 9:
                    octopusGrid[yIndex][xIndex] = 0
                    flashes += 1
        
        if flashes == octopusCount: 
            break
        step += 1
    
    return step

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    octopusGrid = []
    for data in input:
        octopusGrid.append([int(octopus) for octopus in data.replace('\n', '')])

    print(step1(octopusGrid, 100))
    print(step2(octopusGrid)) #Add 100 to results to get final result ¯\_(ツ)_/¯