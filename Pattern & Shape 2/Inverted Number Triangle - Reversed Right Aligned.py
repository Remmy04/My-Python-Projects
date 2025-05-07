rows = 10

for i in range(1, rows+1):
    for j in range(i-1):
        print(" ", end=" ")
    
    for k in range(10, i-1, -1):
        print(k, end=" ")
    
    print()

# Output:
# #   10 9 8 7 6 5 4 3 2 1
# #     10 9 8 7 6 5 4 3 2
# #       10 9 8 7 6 5 4 3
# #         10 9 8 7 6 5 4
# #           10 9 8 7 6 5
# #             10 9 8 7 6
# #               10 9 8 7
# #                 10 9 8
# #                   10 9
# #                     10
# # The above code prints a pattern of numbers in decreasing order.