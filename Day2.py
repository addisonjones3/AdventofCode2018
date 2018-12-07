#!/usr/bin/env python
# TODO Part 1
def part1():
    with open('/Users/ajone2/PycharmProjects/AdventofCode2018/adventofcodeday2.txt', 'r') as f:
        text = f.read().split('\n')

    checkMembers = {'exact2': 0,
                    'exact3': 0}
    # text = ['abcdef',
    #         'bababc',
    #         'abbcde',
    #         'abcccd',
    #         'aabcdd',
    #         'abcdee',
    #         'ababab']
    for code in text:
        letters = list(code)
        letterdict = {}
        twos = []
        threes = []
        for letter in letters:
            if letter in letterdict.keys():
                letterdict[letter] += 1
            else:
                letterdict[letter] = 1

        for letter in letterdict:
            if letterdict[letter] == 2:
                twos.append(letterdict[letter])
            elif letterdict[letter] == 3:
                threes.append(letterdict[letter])

        if len(twos) >= 1:
            checkMembers['exact2'] += 1

        if len(threes) >= 1:
            checkMembers['exact3'] += 1

        # print(code)
        # print(letterdict)
        # loops += 1
        # if loops == 230:
        #     break
    print(checkMembers)
    print(checkMembers['exact2'] * checkMembers['exact3'])

# TODO Part 2

def part2():
    # text = ['abcde',
    #         'fghij',
    #         'klmno',
    #         'pqrst',
    #         'fguij',
    #         'axcye',
    #         'wvxyz']
    with open('/Users/ajone2/PycharmProjects/AdventofCode2018/adventofcodeday2.txt', 'r') as f:
        text = f.read().split('\n')

    checking = True
    sourceindex = 0
    while checking is True:
        sourcecode = text[sourceindex]
        for targetcode in text[sourceindex + 1:]:
            # print('Comparing {0} to {1}'.format(sourcecode, targetcode))
            diffletters = 0
            sameletters = []
            for i, letter in enumerate(targetcode):
                if letter != sourcecode[i]:
                    diffletters += 1
                else:
                    sameletters.append(letter)

                if diffletters > 1:
                    break
            if diffletters == 1:
                return '{0} and {1} share {2}'.format(sourcecode, targetcode, ''.join(sameletters))
        sourceindex += 1

print(part2())
