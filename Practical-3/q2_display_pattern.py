def display_pattern():
    for i in range(1,n+1):
        print("")
        print(" " * (n - i), end="")
        for j in range(1,i+1):
            print(i + 1 - j,end="")

n = int(input("Enter a number: "))
display_pattern()
