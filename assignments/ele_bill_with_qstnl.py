# electricity usage bill generator
# units 0 to 50, Rate=2.60, SC=25
# units 51 to 100, Rate=3.25, SC=35
# units 101 to 200, Rate=5.26, SC=45
# units 200+, Rate=8.45, SC=75

# units = 150


def getBill(x):
    res: float = 0.0
    print()
    if x >= 50: # units 0 to 50, Rate=2.60, SC=25
        print("Pass 1 ✔")
        if x > 50:
            res += 50 * 2.60
        else:
            res += x * 2.60 + 25
    if x >= 51: # units 51 to 100, Rate=3.25, SC=35
        print("Pass 2 ✔")
        if x > 100:
            res += 50 * 3.25
        else:
            res += (x-50) * 3.25 + 35
    if x >= 101: # units 101 to 200, Rate=5.26, SC=45
        print("Pass 3 ✔")
        if x > 200:
            res += 100 * 5.26
        else:
            res += (x-100) * 5.26 + 45
    if x > 200: # units 200+, Rate=8.45, SC=75
        print("Pass 4 ✔")
        res += (x-200) * 8.45 + 75
    print()

    print(f"Your bill amount is {res}")

if __name__ == "__main__":
    x = float(input("Enter the number of units: ")) #number of Units
    getBill(x)