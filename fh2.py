'''with open('f1.txt') as f:
    print(f.read())'''

with open('f1.txt', 'w') as f:
    f.write("hello")

with open('f1.txt', 'a') as f:
    f.write('\tWorld')

with open('f1.txt', 'r') as f:
    print(f.read())


