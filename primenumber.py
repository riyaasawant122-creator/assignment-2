num = int(input("Enter a number: "))

def check():
    count = 0

    for i in range(1,num+1):
        count = count + 1

    if count==2:
        print("prime number")
    else:
        print("not an prime number")

check()                