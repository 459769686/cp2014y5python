print("Miles Kilometers Kilometers Miles")
for i in range(1,10):
    k1 = i * 1.609
    k2 = 15 + i * 5
    m = k2 / 1.609
    print(i,"    ","{0:<10.3f}".format(k1),k2,"      ","{0:<10.3f}".format(m))

k3 = 10 * 1.609
k4 = 65
m1 = k4 / 1.609
print(10,"   ","{0:<10.3f}".format(k3),k4,"       ","{0:<10.3f}".format(m1))
