# Set the number of rows for the triangle pattern
rows = 6

# Outer loop controls the number of rows (from 0 to rows-1)
for i in range(rows):

    # First inner loop prints spaces before the stars to center them
    # The number of spaces decreases with each row
    for j in range(rows - i - 1):
        print(" ", end="")  # Print a space without moving to a new line

    # Second inner loop prints the stars for the current row
    # The number of stars increases with each row (1, 3, 5, 7, ...)
    for j in range(2 * i + 1):
        print("*", end="")  # Print a star without moving to a new line

    # After printing spaces and stars, move to the next line
    print()

# Summary comments:
# This code prints a triangle (or pyramid) pattern with 6 rows.
# The outer loop iterates through each row, while the inner loops handle the spaces and stars for that row.
# The number of spaces starts high and decreases, while the number of stars starts low and increases.
# This creates a centered triangle made of asterisks (*).
# The print() function at the end of each row moves the output to a new line.
