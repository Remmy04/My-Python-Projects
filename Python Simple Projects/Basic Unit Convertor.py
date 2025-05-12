print("Welcome to the Basic Unit Converter!\n")

while True:
    user_input = input("Press any key to continue or 'q' to quit. ")
    print()

    if user_input.lower() == "q":
        print("You have chosen to quit the program.\n")
        print("Thank you for using the Basic Unit Converter!\n")
        print("Goodbye!")
        exit()
    else:
        while True:
            print("Here are the available type of conversions:")
            print("\n1. Length")
            print("2. Weight")
            print("3. Temperature")
            print("4. Volume")
            print("5. Area")
            print("6. Speed")
            print("7. Time")
            print("8. Currency")
            print("9. Energy")
            print("10. Power")
            print("11. Quit\n")

            try:
                number_of_conversions = int(input("Please enter the number of conversions you want to perform (1-11): "))
                if number_of_conversions < 1 or number_of_conversions > 11:
                    print("\nInvalid input. Please enter a number between 1 and 11.\n")
                    continue
                elif number_of_conversions == 1:
                    print("\nYou have chosen to perform LENGTH conversion.\n")
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Kilometers to Miles")
                        print("2. Miles to Kilometers")
                        print("3. Meters to Feet")
                        print("4. Feet to Meters")
                        print("5. Centimeters to Inches")
                        print("6. Inches to Centimeters")
                        print("7. Back to Main Menu")
                    
                        try:
                            num_of_length_conversions = int(input("\nPlease enter the number of length conversions you want to perform (1-7): "))
                            print()
                            if num_of_length_conversions < 1 or num_of_length_conversions > 7:
                                print("Invalid input. Please enter a number between 1 and 7.\n")
                                continue
                            elif num_of_length_conversions == 1:
                                print("You have chosen to convert Kilometers to Miles.\n")
                                print("PLEASE NOTE THAT : 1 kilometer = 0.621371 miles\n")
                                while True:
                                    try:
                                        kilometers = float(input("Please enter the distance in kilometers: "))
                                        miles = kilometers * 0.621371
                                        print("\n" + str(kilometers) + " kilometers = " + str(miles) + " miles.\n")
                                        user_input = input("Do you want to perform another conversion? (y/n) ")
                                        if user_input.lower() == "y":
                                            print()
                                            continue
                                        elif user_input.lower() == "n":
                                            print("\nYou will be redirected to the main menu.\n")
                                            break
                                        else:
                                            print("\nInvalid input. You will be redirected to the main menu.\n")
                                            break
                                    except ValueError:
                                        print("\nInvalid input. Please enter a number.\n")
                                        continue
                                break
                            elif num_of_length_conversions == 2:
                                print("You have chosen to convert Miles to Kilometers.\n")
                                print("PLEASE NOTE THAT : 1 miles = 1.6093445 kilometer\n")
                                while True:
                                    try:
                                        miles = float(input("Please enter the distance in miles: "))
                                        kilometers = miles / 0.621371
                                        print("\n" + str(miles) + " miles = " + str(kilometers) + " kilometers.\n")
                                        user_input = input("Do you want to perform another conversion? (y/n) ")
                                        if user_input.lower() == "y":
                                            print()
                                            continue
                                        elif user_input.lower() == "n":
                                            print("\nYou will be redirected to the main menu.\n")
                                            break
                                        else:
                                            print("\nInvalid input. You will be redirected to the main menu.\n")
                                            break
                                    except ValueError:
                                        print("\nInvalid input. Please enter a number.\n")
                                        continue
                                break
                            elif num_of_length_conversions == 3:
                                print("You have chosen to convert Meters to Feet.\n")
                                print("PLEASE NOTE THAT : 1 meter = 3.28084 feet\n")
                                while True:
                                    try:
                                        meter = float(input("Please enter the distance in meter: "))
                                        feet = meter * 3.28084
                                        print("\n" + str(meter) + " meter = " + str(feet) + " feet.\n")
                                        user_input = input("Do you want to perform another conversion? (y/n) ")
                                        if user_input.lower() == "y":
                                            print()
                                            continue
                                        elif user_input.lower() == "n":
                                            print("\nYou will be redirected to the main menu.\n")
                                            break
                                        else:
                                            print("\nInvalid input. You will be redirected to the main menu.\n")
                                            break
                                    except ValueError:
                                        print("\nInvalid input. Please enter a number.\n")
                                        continue
                                break
                            elif num_of_length_conversions == 4:
                                print("You have chosen to convert Feet to Meters.\n")
                                print("PLEASE NOTE THAT : 1 feet = 0.304799 meter\n")
                                while True:
                                    try:
                                        feet = float(input("Please enter the distance in feet: "))
                                        meter = feet / 3.28084
                                        print("\n" + str(feet) + " feet = " + str(meter) + " meter.\n")
                                        user_input = input("Do you want to perform another conversion? (y/n) ")
                                        if user_input.lower() == "y":
                                            print()
                                            continue
                                        elif user_input.lower() == "n":
                                            print("\nYou will be redirected to the main menu.\n")
                                            break
                                        else:
                                            print("\nInvalid input. You will be redirected to the main menu.\n")
                                            break
                                    except ValueError:
                                        print("\nInvalid input. Please enter a number.\n")
                                        continue
                                break
                            elif num_of_length_conversions == 5:
                                print("You have chosen to convert Centimeters to Inches.\n")
                                print("PLEASE NOTE THAT : 1 centimeters = 0.393701 inches\n")
                                while True:
                                    try:
                                        centimeter = float(input("Please enter the distance in centimeters: "))
                                        inches = centimeter * 0.393701
                                        print("\n" + str(centimeter) + " centimeters = " + str(inches) + " inches.\n")
                                        user_input = input("Do you want to perform another conversion? (y/n) ")
                                        if user_input.lower() == "y":
                                            print()
                                            continue
                                        elif user_input.lower() == "n":
                                            print("\nYou will be redirected to the main menu.\n")
                                            break
                                        else:
                                            print("\nInvalid input. You will be redirected to the main menu.\n")
                                            break
                                    except ValueError:
                                        print("\nInvalid input. Please enter a number.\n")
                                        continue
                                break
                            elif num_of_length_conversions == 6:
                                print("You have chosen to convert Inches to Centimeters.\n")
                                print("PLEASE NOTE THAT : 1 inch = 2.54 centimeters\n")
                                while True:
                                    try:
                                        inches = float(input("Please enter the distance in inches: "))
                                        centimeter = inches / 0.393701
                                        print("\n" + str(inches) + " inches = " + str(centimeter) + " centimeters.\n")
                                        user_input = input("Do you want to perform another conversion? (y/n) ")
                                        if user_input.lower() == "y":
                                            print()
                                            continue
                                        elif user_input.lower() == "n":
                                            print("\nYou will be redirected to the main menu.\n")
                                            break
                                        else:
                                            print("\nInvalid input. You will be redirected to the main menu.\n")
                                            break
                                    except ValueError:
                                        print("\nInvalid input. Please enter a number.\n")
                                        continue
                                break
                            elif num_of_length_conversions == 7:
                                print("You have chosen to go back to the main menu.\n")
                                break
                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 7.\n")
                            continue
                elif number_of_conversions == 2:
                    print("\nYou have chosen to perform WEIGHT conversions.\n")
                    break
                elif number_of_conversions == 3:
                    print("\nYou have chosen to perform TEMPERATURE conversions.\n")
                    break
                elif number_of_conversions == 4:
                    print("\nYou have chosen to perform VOLUME conversions.\n")
                    break
                elif number_of_conversions == 5:
                    print("\nYou have chosen to perform AREA conversions.\n")
                    break
                elif number_of_conversions == 6:
                    print("\nYou have chosen to perform SPEED conversions.\n")
                    break
                elif number_of_conversions == 7:
                    print("\nYou have chosen to perform TIME conversions.\n")
                    break
                elif number_of_conversions == 8:
                    print("\nYou have chosen to perform CURRENCY conversions.\n")
                    break
                elif number_of_conversions == 9:
                    print("\nYou have chosen to perform ENERGY conversions.\n")
                    break
                elif number_of_conversions == 10:
                    print("\nYou have chosen to perform POWER conversions.\n")
                    break
            except ValueError:
                print("\nInvalid input. Please try again and enter a number between 1 and 11.\n")
                continue
