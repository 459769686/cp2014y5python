f = 2
n = int(input("Enter a number: "))
running1 = True
running2 = True

while running1:
    while running2:
        if n % f == 0:
            print(f)
            running2 = False
        else:
            f = f + 1

    running2 = True
    n = n / f
    if n == 1:
        running1 = False
