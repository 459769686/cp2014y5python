def find_gcd():
    running = True
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    if n1 < n2:
        d = n1
    elif n2 < n1:
        d = n2
    else:
        d = n1

    while running:
        if n1 % d == 0 and n2 % d == 0:
            print(d)
            running = False

        d = d - 1

find_gcd()
