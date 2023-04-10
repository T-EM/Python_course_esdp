# sum of odd numbers from 1 to N.

n = int(input("Enter an integer: "))
res = 0
for i in range(1, n+1):
    if i % 2 != 0:
        res += i
print(f"Sum of odd numbers from 1 to {n} is {res}")