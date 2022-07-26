def dec(any):
    def wrap():
        print("I'm calling from main")
        any()
    return wrap
@dec
def f1():
    print('f1')
@dec
def f2():
    print('f2')

'''var=dec(f2)
var()'''

f1()