# sum of the digits of a number

# a = input("Enter an integer: ")
# res = 0
# for d in a:
#     res += int(d)
# print(f"The sum of the digits of {a} is {res}")

a = int(input("Enter an integer: "))
res = 0
num = a
while num != 0:
    rem = num % 10
    res += rem
    num //= 10

print(f"The sum of the digits of {a} is {res}")