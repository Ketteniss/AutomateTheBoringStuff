def a():
    print('a() starts!')
    b()
    d()
    print('a() returns')    
def b():
    print('b() starts!')
    c()
    print('b() returns :(')
def c():
    print('c() start!')
    print('c() returns xD')
def d():
    print('d() starts')
    print('d() returns')
a()