from typing import Tuple


def total1(n,*abc):
    ab=[]
    for i in abc:
        ab.append(i*i)

    return tuple(ab)

print(total1(1,2,3,4,5,6))  