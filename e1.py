def add(a,b):
    try:
        return a+b
    except TypeError as e:
        print('we will not catch exception: Exception')
print(add(2,'4'))