rows = 10  # Total number of rows for the inverted pyramid

for i in range (rows):
    for j in range (i):
        print(" ", end=" ")
    for j in range (2*rows - 1 - 2*i):
        print("*", end=" ")
    print()