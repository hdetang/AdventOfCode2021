import numpy as np

def getBingoDeckAndBoards(input):
    bingoNumbers = [number.replace('\n', '') for number in input]

    filter = set([''])
    bingoNumbers = [number for number in bingoNumbers if number not in filter]

    deck = np.array(bingoNumbers[0].split(','))
    deck = deck.astype(int)

    board = np.empty((5,5))
    count = 0

    boards = []

    for number in bingoNumbers[1:]:
        board[count,:5] = np.array(number.split()).astype(int)
        
        if (count < 4):
            count += 1
            continue

        boards.append(board)
        board = np.empty((5,5))
        count = 0
    return [deck, boards]

def hasBoardWon(drawn, board):
    suites = []

    for i in range(len(board)):
        suites.append([col[i] for col in board])
    
    for row in board:
        suites.append(row)
    
    for suite in suites:
        if len([item for item in suite if item not in drawn]) == 0:
            return True

    return False

def step1(deck, boards):
    drawn = []
    winningBoard = []
    lastDrawn = None

    for number in deck:
        if (len(winningBoard) != 0): break

        drawn.append(number)
        lastDrawn = number

        for board in boards:
            if (hasBoardWon(drawn, board) == True):
                winningBoard = board
                break
    
    return sum([item for item in winningBoard.reshape(-1) if item not in drawn]) * lastDrawn

def step2(deck, boards):
    drawn = []
    winningBoards = []

    for number in deck:
        if(len(boards) == 0): break
        drawn.append(number)

        for index, board in enumerate(boards):
            if (hasBoardWon(drawn, board) == True):
                winningBoards.append([number, board])
                boards.pop(index)
                continue
    
    lastDrawn, winningBoard = winningBoards[-1]

    return sum([item for item in winningBoard.reshape(-1) if item not in drawn]) * lastDrawn

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    deck, boards = getBingoDeckAndBoards(input)

    print(step1(deck, boards))
    print(step2(deck, boards))
