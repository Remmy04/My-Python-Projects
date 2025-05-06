rows = 10

for i in range(rows):          # Loop through 10 rows
    for j in range(i):         # Print i spaces for each row
        print(" ", end="")     # Print space without newline
    print("*")                 # Print the star and move to the next line
