n = int(input("Enter the number: "))
print({i:i*i if i%2==0 else -i*i for i in range(1,n+1)})