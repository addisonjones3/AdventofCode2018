#!/usr/bin/env python

with open('/Users/ajone2/Downloads/adventofcodeday1', 'r') as f:
    text = f.read()
puzzleinput = text.split('\n')

# puzzleinput = ['+1', '-2', '+3', '+1', '+1', '-2']

frequency = 0
freqlist = set()
foundrepeat = False

while foundrepeat is False:
    for input in puzzleinput:
        operator = input[0]
        value = int(input[1:])

        if operator == '+':
            frequency += value
        else:
            frequency -= value

        if frequency in freqlist:
            print('found ' + str(frequency))
            foundrepeat = True
            break
        else:
            freqlist.add(frequency)
print(frequency)


