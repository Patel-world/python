def cout(str):
    val={}
    for i in str:
        val[i]=str.count(i)
    return val

s = input('enter string: ')
d = cout(s)
for i,j in d.items():
    print(f'{i}: {j}')
