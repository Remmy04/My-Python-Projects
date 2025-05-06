def multiply_numbers(a, b):
    return a*b

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

result = multiply_numbers(a, b)

print("The multiply of " + str(a) + " and " + str(b) + " is " + str(result) + ".")