while True:
    try:
        age=int(input("age: "))
        break
    except ValueError:
        print("Try again...")


if(age>18):
    print("can")

else:
    print("can't")