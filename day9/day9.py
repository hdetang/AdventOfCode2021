
def getNeighbors(xPosition, yPosition, heights):
    neighbors = []
    xShape = len(heights[0]) - 1
    yShape = len(heights) - 1

    if (xPosition == 0): neighbors.append([[yPosition, xPosition+1], heights[yPosition][xPosition+1]])
    if (xPosition == xShape): neighbors.append([[yPosition, xPosition-1], heights[yPosition][xPosition-1]])
    if (yPosition == 0): neighbors.append([[yPosition+1, xPosition], heights[yPosition+1][xPosition]])
    if (yPosition == yShape): neighbors.append([[yPosition-1, xPosition], heights[yPosition-1][xPosition]])
    
    if xPosition not in [0, xShape]:
        neighbors.append([[yPosition, xPosition+1], heights[yPosition][xPosition+1]])
        neighbors.append([[yPosition, xPosition-1], heights[yPosition][xPosition-1]])

    if yPosition not in [0, yShape]:
        neighbors.append([[yPosition+1, xPosition], heights[yPosition+1][xPosition]])
        neighbors.append([[yPosition-1, xPosition], heights[yPosition-1][xPosition]])

    return neighbors

def getBasin(point, heights, basin):
    coordinates, _ = point
    y, x = coordinates

    basin.append(point)

    neighbors = getNeighbors(x, y, heights)

    filteredNeighbors = []
    for neighbor in neighbors:
        _, height = neighbor
        if neighbor not in basin and height < 9:
            filteredNeighbors.append(neighbor)

    if len(filteredNeighbors) == 0: return basin

    for neighbor in filteredNeighbors:
        basin = getBasin(neighbor, heights, basin)

    return basin

def step1(heights):
    count = 0

    for yIndex, row in enumerate(heights):
        for xIndex, heigth in enumerate(row):
            neighbors = getNeighbors(xIndex, yIndex, heights)

            isLower = True
            for neighbor in neighbors:
                _, neighborHeight = neighbor
                if neighborHeight > heigth: continue
                isLower = False
                break
            
            if isLower == False: continue
            count += heigth + 1

    return count

def step2(heights):
    largestBasinsCount = []
    lowestPoints = []

    for yIndex, row in enumerate(heights):
        for xIndex, height in enumerate(row):
            neighbors = getNeighbors(xIndex, yIndex, heights)

            isLower = True
            for neighbor in neighbors:
                _, neighborHeight = neighbor
                if neighborHeight > height: continue
                isLower = False
                break
            
            if isLower == False: continue
            lowestPoints.append([[yIndex, xIndex], height])

    for lowestPoint in lowestPoints:
        basin = getBasin(lowestPoint, heights, [])

        unique = []
        for x in basin:
            if x not in unique:
                unique.append(x)

        count = len(unique)
        largestBasinsCount.append(count)
        largestBasinsCount.sort(reverse=True)
    
        if len(largestBasinsCount) > 3: largestBasinsCount.pop(-1)

    return largestBasinsCount[0] * largestBasinsCount[1] * largestBasinsCount[2]

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    heights = []

    for data in input:
        heights.append([int(height) for height in data.replace('\n', '')])
    
    print(step1(heights))
    print(step2(heights))