rows = 10

# Upper half of the diamond (upright pyramid)
for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")
    # Print stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()  # Move to next line

# Lower half of the diamond (inverted pyramid)
for i in range(rows - 2, -1, -1):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")
    # Print stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()  # Move to next line

