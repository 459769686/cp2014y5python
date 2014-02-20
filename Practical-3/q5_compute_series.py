def compute_series():
    print("i  ","m(i)")
    sum = 0
    for i in range(1, 21, 2):
        sum = 0
        for j in range(1, 2 * i + 3, 2):
            if j % 4 == 1:
                sum = sum + 1 / j
            elif j % 4 == 3:
                sum = sum - 1 / j

        print(i," ",sum * 4)

compute_series()
