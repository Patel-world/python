def dec(any):
    def wrap(*arg):
        print("I'm calling from main")
        return any(*arg)
    return wrap
@dec
def f1():
    print('f1')
@dec
def f2():
    print('f2')

@dec
def add(a,b):
    return a+b 

'''var=dec(f2)
var()'''

print(add(5,3))