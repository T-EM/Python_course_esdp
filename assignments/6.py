# to check if the number is divisible by 5 & 6

a = int(input("Enter an integer: "))

if a % 5 == 0:
    print(f"{a} is divisible by 5")
if a % 6 == 0:
    print(f"{a} is divisible by 6")