import csv


with open('f2.txt','r') as f:
    x=[]
    y=[]
    data = csv.reader(f)
    print(data)
    for i in data:
       
        x.append(int(i[0]))
        y.append(int(i[1]))

print(x)
print(y)
