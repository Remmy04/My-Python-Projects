rows = 10

for i in range (rows-1, -1, -1):
    for j in range (rows-i-1):
        print(" ", end=" ")

    for j in range (2*i+1):
        print("*", end=" ")

    print()
    