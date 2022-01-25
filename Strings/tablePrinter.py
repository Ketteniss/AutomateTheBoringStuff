L1 = ['bacon', 'eggs', 'oranges']
L2 = ['coffee', 'milk', 'water']
left = 9
right = 9

"""print('important list'.center(left*2 + 1, '-'))
for i in range(3):
    print(L1[i].rjust(right), L2[i].rjust(right))
"""
def printTable(table):
    adjust = []
    for i in range(len(table)):
        maxlenght = 0
        for str in table[i]:
            if len(str) > maxlenght:
                maxlenght = len(str)
        adjust.append(maxlenght)
    for j in range(len(table[0])):
        for i in range(len(table)):
            print( table[i][j].rjust(adjust[i]),end='  ')
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)