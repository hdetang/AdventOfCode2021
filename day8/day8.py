import numpy as np

def step1(entries):
    count = 0

    for entry in entries:
        patterns, outputs = entry
        for output in outputs:
            if len(output) in [2, 4, 3, 7]:
                count += 1
    return count

if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input = file.readlines()

    entries = []
    raw = [item.replace('\n', '') for item in input]

    for entry in raw:
        patterns, ouput = entry.split('|')
        entries.append([patterns.strip().split(' '), ouput.strip().split(' ')])
    
    print(step1(entries))
