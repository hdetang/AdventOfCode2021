

def step1(lines, pairs):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in lines:
        openedChars = []
        for char in line:
            if char in pairs.keys():
                openedChars.append(char)
                continue

            if pairs[openedChars[-1]] == char :
                openedChars.pop(-1)
                continue

            score += points[char]
            break
    return score

def step2(lines, pairs):
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []

    incompleteOpenedChars = []
    
    for line in lines:
        isIncomplete = True
        openedChars = []
        for char in line:
            if char in pairs.keys():
                openedChars.append(char)
                continue

            if pairs[openedChars[-1]] == char :
                openedChars.pop(-1)
                continue

            isIncomplete = False
            break

        if isIncomplete == True: incompleteOpenedChars.append(openedChars)

    for openedChars in incompleteOpenedChars:
        autocompleteChars = [pairs[char] for char in openedChars]
        autocompleteChars.reverse()
        score = 0
        for char in autocompleteChars:
            score = score * 5 + points[char]
        scores.append(score)

    scores.sort()
    return scores[int(len(scores)/2)]

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()


    input = [item.replace('\n', '') for item in input]
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    print(step1(input, pairs))
    print(step2(input, pairs))