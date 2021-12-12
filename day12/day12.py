
from os import path


def getGraph(input):
    graph = {}

    for path in input:
        start, end = path.split('-')
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)

        if end not in graph:
            graph[end] = [start]
        else:
            graph[end].append(start)
    return graph

visitedList = []

def getPaths(graph, currentVertex, currentPath, paths):
    currentPath.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in currentPath:
            paths = getPaths(graph, vertex, currentPath.copy(), paths)

    paths.append(currentPath)
    return paths

def step1(graph, start, end):
    paths = getPaths(graph, start, [], [])
    
    validPathsCount = 0
    for path in paths:
        if path[-1] == end:
            validPathsCount += 1

    return validPathsCount

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    graph = getGraph([item.replace('\n', '') for item in input])

    print(step1(graph, 'start', 'end'))
