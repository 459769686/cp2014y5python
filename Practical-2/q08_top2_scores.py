running = True
n1 = ""
n2 = ""
t1 = -100
t2 = -200
while running:

    a = str(input("Enter a student's name: "))
    if a == "end":
        print("Highest score: ",n1,t1,"marks")
        print("Second-highest score: ",n2,t2,"marks")
        running = False

    b = int(input("Enter this student's score: "))
    if b > t1:
        t2 = t1
        t1 = b
        n2 = n1
        n1 = a
    elif b < t1 and b > t2:
        t2 = b
        n2 = a
