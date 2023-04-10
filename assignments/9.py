# python program to print even numbers from 1 to n

n = int(input("Enter an integer: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(f"{i} is a even number from 1 to {n}.")