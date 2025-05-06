# filepath: c:\Users\qyean\Desktop\Testing 1.py
while True:
    
    user_input = input("Please enter your grade (0-100) or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Exiting... Bye!")
        break
    try:
        grade = float(user_input)
        if grade < 0 or grade > 100:
            print("Invalid input!")
        elif grade > 55:
            print("You passed!")
        else:
            print("You failed!")
    except ValueError:
        print("Invalid input! Please enter a number.")
