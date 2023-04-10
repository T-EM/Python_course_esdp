# factorial of N

a = int(input("Enter an integer: "))
res = 1
for i in range(1, a+1):
    res *= i
print(f"The factorial of {a} is {res}.")