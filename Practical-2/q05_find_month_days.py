months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
n = int(input("Enter year: "))
m = int(input("Enter month: "))
n1 = n % 4
n2 = n % 100
n3 = n % 400
if n1 == 0 and n2 != 0 and m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print(months[m-1],n,"has 31 days")
elif n1 == 0 and n2 != 0 and m == 2:
    print(months[m-1],n,"has 29 days")
elif n1 == 0 and n2 != 0 and m == 4 or m == 6 or m == 9 or m == 11:
    print(months[m-1],n,"has 30 days")
elif n3 == 0 and m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print(months[m-1],n,"has 31 days")
elif n3 == 0 and m == 2:
    print(months[m-1],n,"has 29 days")
elif n3 == 0 and m == 4 or m == 6 or m == 9 or m == 11:
    print(months[m-1],n,"has 30 days")
else:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print(months[m-1],n,"has 31 days")
    elif m == 2:
        print(months[m-1],n,"has 28 days")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print(months[m-2001],n,"has 30 days")
