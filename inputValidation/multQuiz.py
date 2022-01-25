import time, random, pyinputplus as pyin, sys

numOfQuestions = 10
correctAnswers = 0

gamelog = []
for i in range(numOfQuestions):
    int1 = random.randint(2,15)
    int2 = random.randint(2,15)
    prompt = f'Question Nr. {i+1}\nWhat\'s the product of {int1} and {int2}?\n'
    try:
        answer = pyin.inputStr(prompt, allowRegexes=['^%s$' % (int1 * int2)],
                                       blockRegexes=[('.*', 'Incorrect!')],
                                       timeout=8, limit=3)
        gamelog.append(((int1,int2), int1*int2, answer))
        

    except pyin.TimeoutException:
        print('Out of time!')
        gamelog.append(((int1,int2), int1*int2, answer))
    except pyin.RetryLimitException:
        print('Out of tries!')
        gamelog.append(((int1,int2), int1*int2, answer))
    else: 
        print('Correct!')
        correctAnswers += 1
    time.sleep(0.5) # Brief pause to let user see the result.
    

print(f'Result: You answered {correctAnswers} of 10 questions correctly.')
showResults = pyin.inputYesNo('Do you want to see the actual results?\n')    
if showResults == 'yes':
    for round, result in enumerate(gamelog):
        print('#%s: %s * %s = %s'.rjust(15) % (round+1, result[0][0], result[0][1], result[1]), end='')
        print(f'Your Answer: {result[2]}'.rjust(5))
else:
    print("Thanks for playing!")
    sys.exit()
