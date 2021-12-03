import numpy as np

def getBitsByIndex(reports):
    bitsByIndex = []

    for report in reports:
        for index, bit in enumerate(report):
            if (len(bitsByIndex) <= index):
                bitsByIndex.append(bit)
                continue
            bitsByIndex[index] += bit
    return bitsByIndex

def step1(reports):
    epsilonRate = ''
    gammaRate = ''

    bitsByIndex = getBitsByIndex(reports)

    for bits in bitsByIndex:
        bitsList, count = np.unique(np.array(list(bits)).reshape(-1), axis=0, return_counts=True)

        mostCommonBit = bitsList[count.argmax()]
        leastCommonBit = bitsList[count.argmin()]

        gammaRate += mostCommonBit
        epsilonRate += leastCommonBit

    return int(epsilonRate, 2) * int(gammaRate,2)

def step2(reports):
    filteredOxygenRate = np.array(reports)
    filteredCo2Rate = np.array(reports)
    reportLength = len(reports[0])

    for index in range(reportLength):
        oxygenFilter = []
        co2Filter = []

        if len(filteredOxygenRate) != 1:
            bitsByIndex = getBitsByIndex(filteredOxygenRate)
            bitsList, count = np.unique(np.array(list(bitsByIndex[index])).reshape(-1), axis=0, return_counts=True)
            mostCommonBit = bitsList[count.argmax()]
            if len(count) > 1 and count[0] == count[1]: mostCommonBit = '1'
            
            for report in filteredOxygenRate:
                oxygenFilter.append(report[index] == mostCommonBit)
            filteredOxygenRate = filteredOxygenRate[oxygenFilter]


        if len(filteredCo2Rate) != 1:
            bitsByIndex = getBitsByIndex(filteredCo2Rate)
            bitsList, count = np.unique(np.array(list(bitsByIndex[index])).reshape(-1), axis=0, return_counts=True)
            leastCommonBit = bitsList[count.argmin()]
            if len(count) > 1 and count[0] == count[1]: leastCommonBit = '0'
            
            for report in filteredCo2Rate:
                co2Filter.append(report[index] == leastCommonBit)
            filteredCo2Rate = filteredCo2Rate[co2Filter]

    return int(filteredOxygenRate[0], 2) * int(filteredCo2Rate[0], 2)

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    reports = [report.replace('\n', '') for report in input]
    print(step1(reports))
    print(step2(reports))
