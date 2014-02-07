running = True
n = 50

while running:
    i = n * n * n
    if i < 12000:
        print(n)
        running = False

    n = n - 1
