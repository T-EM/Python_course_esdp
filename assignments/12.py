# count the number of digits in the given number

# a = input("Enter an integer: ")
# print(f"The number of digits in the {a} is {len(a)}.")

n = int(input("Enter an integer: "))
res = 0
for i in range(1, n+1):
    if i % 2 != 0:
        res += 1
print(f"Sum of odd numbers from 1 to {n} is {res}")