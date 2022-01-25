def collatz(number):
    if (number % 2 == 0):
        n = number // 2
        print(n)
        return n
    else:
        n = 3 * number + 1
        print(n)
        return n

def whileNotOne():
    
        while True:
            try:
                print('Type in any positive integer:', end='')
                userNum = int(input())
                if userNum > 0:
                    print('Bad input!')
                    break 
            except:
                print('Bad input!')
                continue
        while True:            
            c = collatz(userNum)
            if c == 1:
                print('Collatz!')
                break
            userNum = c
    
whileNotOne()