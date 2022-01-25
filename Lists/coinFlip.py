import random

def main():
    result = experiment(10000, 100, 10)
    print('Chance of streak: %s%%' % result)

def experiment(times, flips, streakSize):
    numberOfStreaks = 0
    for _ in range(times):
        if coinFlips(flips, streakSize):
            numberOfStreaks += 1
    return numberOfStreaks/100

def coinFlips(flips, streakSize):
    FlipSequence = []
    consFlips = 0
    for i in range(flips):
        flipResult = random.randint(0,1)
        FlipSequence.append(flipResult)
        if i >= 1:
            if FlipSequence[i-1] == FlipSequence[i]:
                consFlips += 1
            else:
                if consFlips == streakSize:
                    return True
                consFlips = 0
main()