def convert_ms():
    n = int(input("Enter milliseconds: "))
    n = n // 1000
    s = n % 60
    m = (n // 60) % 60
    h = n // 3600
    print(h,":",m,":",s)

h = 0
m = 0
s = 0
convert_ms()
