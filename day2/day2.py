def step1(instructions):
    xAxis = 0
    yAxis = 0

    for instruction in instructions:
        splittedInstruction = instruction.split()
        unit = int(splittedInstruction[1])

        match splittedInstruction[0]:
            case 'forward':
                xAxis += unit
            case 'up':
                yAxis -= unit
            case 'down':
                yAxis += unit

    return xAxis * yAxis

def step2(instructions):
    xAxis = 0
    yAxis = 0
    aim = 0

    for instruction in instructions:
        splittedInstruction = instruction.split()
        unit = int(splittedInstruction[1])

        match splittedInstruction[0]:
            case 'forward':
                xAxis += unit
                yAxis += aim*unit
            case 'up':
                aim -= unit
            case 'down':
                aim += unit

    return xAxis * yAxis

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    print(step1(input))
    print(step2(input))
