num = int(input("Please enter a number : "))
factorial = 1
for i in range (1, num + 1):
    factorial *= i

print("The factorial of " + str(num) + " is " + str(factorial) + ".")
