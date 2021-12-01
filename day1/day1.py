def step1(measurements):
    previousDepth = None
    count = 0

    for measurement in measurements:
        depth = int(measurement)

        if previousDepth is not None and depth > previousDepth:
            count += 1

        previousDepth = depth

    return count

def step2(measurements):
    count = 0
    previousSum = None

    for index, measurement in enumerate(measurements):
        depth = int(measurement)

        if index <= 1:
            continue

        sum = depth + int(measurements[index - 1]) + int(measurements[index - 2])

        if previousSum is not None and sum > previousSum:
            count += 1
        previousSum = sum

    return count

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input = file.readlines()

    print(step1(input))
    print(step2(input))
