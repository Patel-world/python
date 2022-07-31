f=open(r'C:\Users\panka\Desktop\python-t\f1.txt')
print(f.tell())
print('\n')
print(f.read())
print('\n')

print(f.tell())
f.seek(33)
print(f.read())
f.seek(0)
s=f.read()
z=[]
print(s)

for  i in s:
    if i == '+':
        break
    z.append(i)

listToStr = ''.join(map(str, z))
print('qwr\n')
print(listToStr)
f.close()