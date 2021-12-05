import numpy as np

def getLines(input):
    raw = [number.replace('\n', '').replace(' ', '') for number in input]
    lines= []
    width = 0
    height = 0

    for data in raw:
        row = data.split('->')

        start = [int(item) for item in row[0].split(',')]
        end = [int(item) for item in row[1].split(',')]

        maxX = max([start[0], end[0]])
        maxY = max([start[1], end[1]])

        if maxX > width: width = maxX
        if maxY > height: height = maxY

        lines.append([start, end])
            
    return [lines, (height, width)]

def buildDiagram(lines, shape):
    diagram = np.zeros(shape)

    for coordinates in lines:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if (x1 == x2):
            start, end = [y1, y2] if y1 < y2 else [y2, y1]
            diagram[x1, start:end] = [item+1 for item in diagram[x1, start:end]]

        if (y1 == y2):
            start, end = [x1, x2] if x1 < x2 else [x2, x1]
            diagram[start:end, y1] = [item+1 for item in diagram[start:end, y1]]

    return diagram

def step1(diagram):
    overlappingLines = []
    count = 0
    for yIndex, column in enumerate(diagram):
        for xIndex, row in enumerate(column):
            if row >= 2: 
                count += 1
                continue
            continue
            count += 1
            print(row, count)

            position = [xIndex, yIndex]
            if position not in overlappingLines: overlappingLines.append(position)

            nextPosition = xIndex + 1
            while nextPosition <= 990 or diagram[nextPosition, yIndex] > 1:
                overlappingLines.append([nextPosition, yIndex])
                if nextPosition == 990: break
                nextPosition += 1
    
            previousPosition = xIndex - 1
            while previousPosition >= 0 or diagram[previousPosition, yIndex] > 1:
                overlappingLines.append([previousPosition, yIndex])
                if nextPosition == 0: break
                nextPosition -= 1
                
            nextPosition = yIndex + 1
            while nextPosition <= 990 or diagram[xIndex, nextPosition] > 1:
                overlappingLines.append([xIndex, nextPosition])
                if nextPosition == 990: break
                nextPosition += 1
    
            previousPosition = yIndex - 1
            while previousPosition >= 0 or diagram[xIndex, previousPosition] > 1:
                overlappingLines.append([xIndex, previousPosition])
                if nextPosition == 0: break
                nextPosition -= 1


    return count

def step2(diagram):
    return 'toto'

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    lines, shape = getLines(input)
    diagram = buildDiagram(lines, shape)

    print(step1(diagram))
    #print(step2(deck, boards))
