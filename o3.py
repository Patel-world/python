class person:
    i=0
    def __init__(self,a,b,c):
        person.i+=1
        self.first_name=a
        self.last_name=b
        self.__age=c
        self.name=a+" " +b
    def intro(self,n):
        return f"{n}! myself {self.name} age {self.__age}"



p1=person('qwerty','lost',22)
p1._person__age=21


print(p1.first_name)
print(p1.name)
print(p1.intro("hello"))

print(p1.__dict__)


