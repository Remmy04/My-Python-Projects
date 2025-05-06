rows = 10

for i in range (rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Print \ and move the cursor to the next line

# This code prints a right-angled triangle pattern of asterisks (*) with 10 rows.   
# print(): This moves the cursor to the next line, but it doesn't print any characters on that line. It's like saying, "Okay, let's go to the next line now."
# It's not printing a blank line with spaces; it's simply moving to the next line for your next output.
# So, in this case, after printing the stars for a row, the print() function ensures that the next set of stars appears on the next line, rather than continuing on the same line.