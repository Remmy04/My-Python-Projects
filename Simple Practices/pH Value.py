while True:
    user_input = input("Please enter your pH value (0-14) or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Exiting... Bye!")
        break
    try:
        pH = float(user_input)
        if pH < 0 or pH > 14:
            print("Invalid input!")
        elif pH > 7:
            print("Basic")
        elif pH < 7:
            print("Acidic")
        else:
            print("Neutral")
    except ValueError:
        print("Invalid input! Please enter a number.")
