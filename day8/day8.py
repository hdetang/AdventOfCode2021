def getMapping(patterns):
    digits = {}

    fiveDigitPatterns = []
    sixDigitPatterns = []

    for pattern in patterns:
        sortedPattern = ''.join(sorted(pattern))

        match len(sortedPattern):
            case 2:
                digits['1'] = sortedPattern
            case 3:
                digits['7'] = sortedPattern
            case 4: 
                digits['4'] = sortedPattern
            case 5:
                fiveDigitPatterns.append(sortedPattern)
            case 6:
                sixDigitPatterns.append(sortedPattern)
            case 7: 
                digits['8'] = sortedPattern
    
    almostNine = list(set(digits['7']) - set(digits['1']))[0] + digits['4']
    letterG = None
    for pattern in sixDigitPatterns:
        difference = list(set(pattern) - set(almostNine))
        if len(difference) == 1:
            digits['9'] = pattern
            letterG = difference[0]
            sixDigitPatterns.remove(digits['9'])
            break

    for pattern in sixDigitPatterns:
        difference = list(set(digits['9']) - set(pattern))
        if len(difference) == 0: continue
        if len(difference) == 1 and difference[0] in digits['1']:
            digits['6'] = pattern
            sixDigitPatterns.remove(digits['6'])
            break

    digits['0'] = sixDigitPatterns[0]

    almostThree = ''.join(sorted(digits['7'] + letterG))    
    for pattern in fiveDigitPatterns:
        if len(set(pattern) - set(almostThree)) == 1:
            digits['3'] = pattern
            fiveDigitPatterns.remove(digits['3'])
            break

    for pattern in fiveDigitPatterns:
        difference = list(set(digits['9']) - set(pattern))
        if len(difference) == 0: continue
        if len(difference) == 1 and difference[0] in digits['1']:
            digits['5'] = pattern
            fiveDigitPatterns.remove(digits['5'])
            break
    
    digits['2'] = fiveDigitPatterns[0]

    return {value: key for key, value in digits.items()}

def step1(entries):
    count = 0

    for entry in entries:
        _, outputs = entry
        for output in outputs:
            if len(output) in [2, 4, 3, 7]:
                count += 1
    return count

def step2(entries):
    count = 0

    for entry in entries:
        patterns, outputs = entry
        mapping = getMapping(patterns)
        decoded = ''
    
        for output in outputs:
            decoded += mapping[''.join(sorted(output))]
        
        count += int(decoded)

    return count

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    entries = []
    raw = [item.replace('\n', '') for item in input]

    for entry in raw:
        patterns, ouputs = entry.split('|')
        entries.append([patterns.strip().split(' '), ouputs.strip().split(' ')])

    print(step1(entries))
    print(step2(entries))