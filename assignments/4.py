# check if the number is positive or negative

a = int(input("Enter an integer: "))
if a == 0:
    print("The number is neither positive nor negative.")
elif a > 0:
    print("The number is positive.")
else:
    print("The number is negative.")