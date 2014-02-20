def m_series():
    sum = 0
    print("i   ","m(i)")
    for i in range(1, 20):
        sum = sum + i / (i + 1)
        print(i," ","{0:<10.4f}".format(sum))

m_series()
