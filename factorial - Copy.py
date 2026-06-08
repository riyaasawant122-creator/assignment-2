num = int(input("Enter your number: "))

def check():
    fact = 1
    for i in range(1,num + 1):
        fact = fact * i
    print("Factorial of number is: ",fact)

check()    