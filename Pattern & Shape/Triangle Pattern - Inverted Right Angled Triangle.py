rows = 10  # Total number of rows in the triangle

# Outer loop controls the number of rows
for i in range(rows):
    
    # Inner loop prints decreasing number of stars in each row
    # It starts with 10 stars and decreases by 1 in every new row
    for j in range(rows - i):
        print("*", end="")  # Print star and stay on the same line
    
    print()  # Move to the next line after each row is printed

