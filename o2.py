class person:
    i=0
    def __init__(self,a,b,c):
        person.i+=1
        self.first_name=a
        self.last_name=b
        self._age=c
        self.name=a+" " +b
    def intro(self,n):
        return f"{n}! myself {self.name} age {self._age}"

class data(person):
    new_line = '\n'
    def __init__(self, a,b,c,d):
        super().__init__(a,b,c)
        self.address=d
    def full_intro(self):
        return f"{self.name}{data.new_line}{self._age}{data.new_line}from {self.address}"


class super_data(data):
    new_line = '\n'
    def __init__(self, a,b,c,d,e):
        data.__init__(self,a,b,c,d)
        self.__contact=e
    def super_full_intro(self):
        return f"{self.name}{data.new_line}{self._age}{data.new_line}from {self.address}{data.new_line}contact: {self.__contact}"


p1=person('qwerty','lost',22)

p2=person('qwerty','lost',22)
p3=data('qwerty','lost',22,'jupiter')
p4=super_data('qwerty','lost',22,'jupiter','T-222136')
p4._super_data__contact = 'T-221206'
p3._age=21
'''print(p1.first_name)
print(p1.name)
print(p1.intro("hello"))
print(person.i)'''

print(p1.__dict__)
print(p4.super_full_intro())

