rows = 10

for i in range(1, rows+1):
    for j in range (i-1):
        print(" ", end=" ")

    for k in range(1, rows-i+2):
        print(k, end=" ")

    print()

# Output:
# #   1 2 3 4 5 6 7 8 9 10
# #     1 2 3 4 5 6 7 8 9
# #       1 2 3 4 5 6 7 8
# #         1 2 3 4 5 6 7
# #           1 2 3 4 5 6
# #             1 2 3 4 5
# #               1 2 3 4
# #                 1 2 3
# #                   1 2
# #                     1
# # The above code prints a pattern of numbers in decreasing order.
    