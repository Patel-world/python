def total(*abc):
    s=0
    for i in abc:
        s=s+i
    return s

print(total(1,3,5,9,8))        


def total1(n,n1,*abc):
    s=0
    for i in abc:
        s=s+i
    return s

print(total1(1,2,3,4,5,6))        