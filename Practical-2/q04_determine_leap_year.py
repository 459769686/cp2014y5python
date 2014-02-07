n = int(input("Enter year: "))
n1 = n % 4
n2 = n % 100
n3 = n % 400
if n1 == 0 and n2 != 0:
    print("Leap")
elif n3 == 0:
    print("Leap")
else:
    print("Non-leap")
