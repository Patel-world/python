class person:
    def __init__(self,a,b,c):
        self.first_name=a
        self.last_name=b
        self.age=c
        self.name=a+" " +b

p1=person('qwerty','lost',22)
print(p1.first_name)
print(p1.name)