rows = 10

for i in range (1, rows+1):
    for j in range(rows-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print(j, end=" ")
    
    print()

# Output:
# #                     1 
# #                   1 2
# #                 1 2 3
# #               1 2 3 4
# #             1 2 3 4 5
# #           1 2 3 4 5 6
# #         1 2 3 4 5 6 7
# #       1 2 3 4 5 6 7 8
# #     1 2 3 4 5 6 7 8 9
# #   1 2 3 4 5 6 7 8 9 10
# # The above code prints a right-aligned number triangle pattern.