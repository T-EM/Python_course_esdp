# find all the divisors of an integer

a = int(input("Enter an integer: "))

for i in range(1, a+1):
    if a % i == 0:
        print(f"{i} is the divisor of {a}.")