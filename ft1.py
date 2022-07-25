def cout(str):
    k=0
    l=0
    for i in str:
        if(i.isdigit()):
            k=k+1
        else:
            l=l+1
    return f"Number of digits in string are {k} and letters are {l}"

n = input("enter string: ")
print(cout(n))