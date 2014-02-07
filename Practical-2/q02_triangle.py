a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a + b <= c or b + c <= a or c + a <= b:
    print("Invalid Triangle!")
else:
    P = a + b + c
    print("Perimeter = ", P)
