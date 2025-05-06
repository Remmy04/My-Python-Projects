rows = 10  # Total number of rows for the triangle

# Outer loop controls the number of rows
for i in range(rows):
    
    # First inner loop prints spaces to push the stars to the right
    # Number of spaces decreases as 'i' increases
    for j in range(rows - i - 1):
        print(" ", end="")  # Print space and stay on the same line
    
    # Second inner loop prints stars after the spaces
    # Number of stars increases with each row
    for j in range(i + 1):
        print("*", end="")  # Print star and stay on the same line
    
    print()  # Move to the next line after each row is printed
