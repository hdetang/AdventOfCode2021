import numpy as np
import cv2 as cv

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
            end += 1
            diagram[x1, start:end] = [item+1 for item in diagram[x1, start:end]]
            continue

        if (y1 == y2):
            start, end = [x1, x2] if x1 < x2 else [x2, x1]
            end += 1
            diagram[start:end, y1] = [item+1 for item in diagram[start:end, y1]]
            continue

    #cv.imshow('diagram', diagram)
    #cv.waitKey()
    return diagram

def step1(diagram):
    overlappingLines = []
    count = 0
    for yIndex, column in enumerate(diagram):
        for xIndex, row in enumerate(column):
            if row >= 2: 
                count += 1

    return count

def step2(diagram):
    return 'toto'

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    lines, shape = getLines(input)
    diagram = buildDiagram(lines, shape)

    print(step1(diagram))
    print(test(lines))
    #print(step2(deck, boards))
