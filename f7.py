l1 = [1, 2, 3, 4]
l2= [5,6,7,8]

x=dict(zip(l1,l2))

print(x)
y=[]
for i,j in x.items():
    y.append((i+j)/2)

print(y)