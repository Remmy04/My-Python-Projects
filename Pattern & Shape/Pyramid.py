rows = 10

for i in range (rows):
    for j in range (rows-i-1):
        print(" ", end=" ")
    for j in range (2*i + 1):
        print("*", end=" ")
    print()

# The above code prints a pyramid pattern of stars. 
# The outer loop iterates through the number of rows, while the inner loops handle the spaces and stars for each row. 
# The first inner loop prints spaces to center the stars, and the second inner loop prints the stars, increasing the count with each row.
# The result is a pyramid shape made of stars, with the base being the widest part and the top being a single star.
# The pyramid pattern is a common exercise in programming, often used to practice nested loops and control structures.  