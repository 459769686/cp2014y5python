def reverse_int():
    number = str(n)
    lst = [number[i] for i in range(len(number))]
    lst.reverse()
    print("".join(lst))

n = input("Enter a number: ")
reverse_int()
