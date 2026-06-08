num = int(input("enter a number: "))

def check():
    n = num
    s = 0

    while num > 0:
        digit = n % 10
        s = s+digit
        n = n // 10

    print("Sum of digit is:", s)

check()        