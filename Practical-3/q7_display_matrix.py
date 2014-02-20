import random
def print_matrix():
    print(random.randint(0, 1),"",end="")


n = int(input("Enter a number: "))
for i in range(1, n + 1):

    for j in range(1, n + 1):
        print_matrix()

    print()
