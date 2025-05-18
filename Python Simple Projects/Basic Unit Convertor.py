print("Welcome to the Basic Unit Converter!\n")

while True:
    user_input = input("Press Enter to continue or type 'q' to quit: ")
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
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Kilograms to Pounds")
                        print("2. Pounds to Kilograms")
                        print("3. Grams to Ounces")
                        print("4. Ounces to Grams")
                        print("5. Back to Main Menu")
                    
                        try:
                            num_of_weight_conversions = int(input("\nPlease enter the number of weight conversions you want to perform (1-5): "))
                            print()
                            if num_of_weight_conversions < 1 or num_of_weight_conversions > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue
                            elif num_of_weight_conversions == 1:
                                print("You have chosen to convert Kilograms to Pounds.\n")
                                print("PLEASE NOTE THAT : 1 kilogram = 2.20462 pounds\n")
                                while True:
                                    try:
                                        kilograms = float(input("Please enter the weight in kilograms: "))
                                        pounds = kilograms * 2.20462
                                        print("\n" + str(kilograms) + " kilograms = " + str(pounds) + " pounds.\n")
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
                            elif num_of_weight_conversions == 2:
                                print("You have chosen to convert Pounds to Kilograms.\n")
                                print("PLEASE NOTE THAT : 1 pounds = 0.453592 kilograms\n")
                                while True:
                                    try:
                                        pounds = float(input("Please enter the weight in pounds: "))
                                        kilograms = pounds / 2.20462
                                        print("\n" + str(pounds) + " pounds = " + str(kilograms) + " kilograms.\n")
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
                            elif num_of_weight_conversions == 3:
                                print("You have chosen to convert Grams to Ounces.\n")
                                print("PLEASE NOTE THAT : 1 gram = 0.035274 ounce\n")
                                while True:
                                    try:
                                        grams = float(input("Please enter the weight in grams: "))
                                        ounces = grams * 0.035274
                                        print("\n" + str(grams) + " grams = " + str(ounces) + " ounces.\n")
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
                            elif num_of_weight_conversions == 4:
                                print("You have chosen to convert Ounces to Grams.\n")
                                print("PLEASE NOTE THAT : 1 ounce = 28.3495 grams \n")
                                while True:
                                    try:
                                        ounces = float(input("Please enter the weight in ounces: "))
                                        grams = ounces / 0.035274
                                        print("\n" + str(ounces) + " ounces = " + str(grams) + " grams.\n")
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
                            elif num_of_weight_conversions == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break
                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue
                elif number_of_conversions == 3:
                    print("\nYou have chosen to perform TEMPERATURE conversions.\n")
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Celsius to Fahrenheit")
                        print("2. Fahrenheit to Celsius")
                        print("3. Kelvin to Celsius")
                        print("4. Celsius to Kelvin")
                        print("5. Back to Main Menu")
                    
                        try:
                            num_of_temperature_conversions = int(input("\nPlease enter the number of temperature conversions you want to perform (1-5): "))
                            print()
                            if num_of_temperature_conversions < 1 or num_of_temperature_conversions > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue
                            elif num_of_temperature_conversions == 1:
                                print("You have chosen to convert Celsius to Fahrenheit.\n")
                                print("PLEASE NOTE THAT : 1 Celsius = 33.8 Fahrenheit\n")
                                while True:
                                    try:
                                        celsius = float(input("Please enter the temperature in Celsius: "))
                                        fahrenheit = celsius * 9/5 + 32
                                        print("\n" + str(celsius) + " degrees Celsius = " + str(fahrenheit) + " degrees Fahrenheit.\n")
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
                            elif num_of_temperature_conversions == 2:
                                print("You have chosen to convert Fahrenheit to Celsius.\n")
                                print("PLEASE NOTE THAT : 1 Fahrenheit = -17.2222 Celsius\n")
                                while True:
                                    try:
                                        fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
                                        celsius = (fahrenheit - 32) * 5/9
                                        print("\n" + str(fahrenheit) + " degrees Fahrenheit = " + str(celsius) + " degrees Celsius.\n")
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
                            elif num_of_temperature_conversions == 3:
                                print("You have chosen to convert Kelvin to Celsius.\n")
                                print("PLEASE NOTE THAT : 1 Kelvin = -272.15 Celsius\n")
                                while True:
                                    try:
                                        kelvin = float(input("Please enter the temperature in Kelvin: "))
                                        celsius = (kelvin - 273.15)
                                        print("\n" + str(kelvin) + " degrees Kelvin = " + str(celsius) + " degrees Celsius.\n")
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
                            elif num_of_temperature_conversions == 4:
                                print("You have chosen to convert Celsius to Kelvin.\n")
                                print("PLEASE NOTE THAT : 1 Celsius = 274.15 Kelvin\n")
                                while True:
                                    try:
                                        celsius = float(input("Please enter the temperature in Celsius: "))
                                        kelvin = celsius + 273.15
                                        print("\n" + str(celsius) + " degrees Celsius = " + str(kelvin) + " degrees Kelvin.\n")
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
                            elif num_of_temperature_conversions == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break
                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue
                elif number_of_conversions == 4:
                    print("\nYou have chosen to perform VOLUME conversions.\n")
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Liters to Gallons")
                        print("2. Gallons to Liters")
                        print("3. Milliliters to Fluid Ounces")
                        print("4. Fluid Ounces to Milliliters")
                        print("5. Cubic Meters to Cubic Feet")
                        print("6. Cubic Feet to Cubic Meters")
                        print("7. Back to Main Menu")

                        try:
                            num_of_volume_conversions = int(input("\nPlease enter the number of volume conversions you want to perform (1-7): "))
                            print()
                            if num_of_volume_conversions < 1 or num_of_volume_conversions > 7:
                                print("Invalid input. Please enter a number between 1 and 7.\n")
                                continue
                            elif num_of_volume_conversions == 1:
                                print("You have chosen to convert Liters to Gallons.\n")
                                print("PLEASE NOTE THAT : 1 Liter = 0.264172 Gallons\n")
                                while True:
                                    try:
                                        liters = float(input("Please enter the volume in Liters: "))
                                        gallons = liters * 0.264172
                                        print("\n" + str(liters) + " liters = " + str(gallons) + " gallons.\n")
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
                            elif num_of_volume_conversions == 2:
                                print("You have chosen to convert Gallons to Liters.\n")
                                print("PLEASE NOTE THAT : 1 Gallon = 3.78541 Liters\n")
                                while True:
                                    try:
                                        gallons = float(input("Please enter the volume in Gallons: "))
                                        liters = gallons * 3.78541
                                        print("\n" + str(gallons) + " gallons = " + str(liters) + " liters.\n")
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
                            elif num_of_volume_conversions == 3:
                                print("You have chosen to convert Milliliters to Fluid Ounces.\n")
                                print("PLEASE NOTE THAT : 1 Milliliter = 0.033814 Fluid Ounces\n")
                                while True:
                                    try:
                                        ml = float(input("Please enter the volume in Milliliters: "))
                                        fl_oz = ml * 0.033814
                                        print("\n" + str(ml) + " milliliters = " + str(fl_oz) + " fluid ounces.\n")
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
                            elif num_of_volume_conversions == 4:
                                print("You have chosen to convert Fluid Ounces to Milliliters.\n")
                                print("PLEASE NOTE THAT : 1 Fluid Ounce = 29.5735 Milliliters\n")
                                while True:
                                    try:
                                        fl_oz = float(input("Please enter the volume in Fluid Ounces: "))
                                        ml = fl_oz * 29.5735
                                        print("\n" + str(fl_oz) + " fluid ounces = " + str(ml) + " milliliters.\n")
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
                            elif num_of_volume_conversions == 5:
                                print("You have chosen to convert Cubic Meters to Cubic Feet.\n")
                                print("PLEASE NOTE THAT : 1 Cubic Meter = 35.3147 Cubic Feet\n")
                                while True:
                                    try:
                                        m3 = float(input("Please enter the volume in Cubic Meters: "))
                                        ft3 = m3 * 35.3147
                                        print("\n" + str(m3) + " cubic meters = " + str(ft3) + " cubic feet.\n")
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
                            elif num_of_volume_conversions == 6:
                                print("You have chosen to convert Cubic Feet to Cubic Meters.\n")
                                print("PLEASE NOTE THAT : 1 Cubic Foot = 0.0283168 Cubic Meters\n")
                                while True:
                                    try:
                                        ft3 = float(input("Please enter the volume in Cubic Feet: "))
                                        m3 = ft3 * 0.0283168
                                        print("\n" + str(ft3) + " cubic feet = " + str(m3) + " cubic meters.\n")
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
                            elif num_of_volume_conversions == 7:
                                print("You have chosen to go back to the main menu.\n")
                                break
                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 7.\n")
                            continue
                elif number_of_conversions == 5:
                    print("\nYou have chosen to perform AREA conversions.\n")
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Square Meters to Square Feet")
                        print("2. Square Feet to Square Meters")
                        print("3. Acres to Square Meters")
                        print("4. Square Meters to Acres")
                        print("5. Square Kilometers to Square Miles")
                        print("6. Square Miles to Square Kilometers")
                        print("7. Back to Main Menu")

                        try:
                            num_of_area_conversions = int(input("\nPlease enter the number of area conversions you want to perform (1-7): "))
                            print()
                            if num_of_area_conversions < 1 or num_of_area_conversions > 7:
                                print("Invalid input. Please enter a number between 1 and 7.\n")
                                continue
                            elif num_of_area_conversions == 1:
                                print("You have chosen to convert Square Meters to Square Feet.\n")
                                print("PLEASE NOTE THAT : 1 Square Meter = 10.7639 Square Feet\n")
                                while True:
                                    try:
                                        sqm = float(input("Please enter the area in Square Meters: "))
                                        sqft = sqm * 10.7639
                                        print("\n" + str(sqm) + " square meters = " + str(sqft) + " square feet.\n")
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
                            elif num_of_area_conversions == 2:
                                print("You have chosen to convert Square Feet to Square Meters.\n")
                                print("PLEASE NOTE THAT : 1 Square Foot = 0.092903 Square Meters\n")
                                while True:
                                    try:
                                        sqft = float(input("Please enter the area in Square Feet: "))
                                        sqm = sqft * 0.092903
                                        print("\n" + str(sqft) + " square feet = " + str(sqm) + " square meters.\n")
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
                            elif num_of_area_conversions == 3:
                                print("You have chosen to convert Acres to Square Meters.\n")
                                print("PLEASE NOTE THAT : 1 Acre = 4046.86 Square Meters\n")
                                while True:
                                    try:
                                        acres = float(input("Please enter the area in Acres: "))
                                        sqm = acres * 4046.86
                                        print("\n" + str(acres) + " acres = " + str(sqm) + " square meters.\n")
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
                            elif num_of_area_conversions == 4:
                                print("You have chosen to convert Square Meters to Acres.\n")
                                print("PLEASE NOTE THAT : 1 Square Meter = 0.000247105 Acres\n")
                                while True:
                                    try:
                                        sqm = float(input("Please enter the area in Square Meters: "))
                                        acres = sqm * 0.000247105
                                        print("\n" + str(sqm) + " square meters = " + str(acres) + " acres.\n")
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
                            elif num_of_area_conversions == 5:
                                print("You have chosen to convert Square Kilometers to Square Miles.\n")
                                print("PLEASE NOTE THAT : 1 Square Kilometer = 0.386102 Square Miles\n")
                                while True:
                                    try:
                                        sqkm = float(input("Please enter the area in Square Kilometers: "))
                                        sqmi = sqkm * 0.386102
                                        print("\n" + str(sqkm) + " square kilometers = " + str(sqmi) + " square miles.\n")
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
                            elif num_of_area_conversions == 6:
                                print("You have chosen to convert Square Miles to Square Kilometers.\n")
                                print("PLEASE NOTE THAT : 1 Square Mile = 2.58999 Square Kilometers\n")
                                while True:
                                    try:
                                        sqmi = float(input("Please enter the area in Square Miles: "))
                                        sqkm = sqmi * 2.58999
                                        print("\n" + str(sqmi) + " square miles = " + str(sqkm) + " square kilometers.\n")
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
                            elif num_of_area_conversions == 7:
                                print("You have chosen to go back to the main menu.\n")
                                break
                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 7.\n")
                        continue
                    
                elif number_of_conversions == 6:
                    print("\nYou have chosen to perform SPEED conversions.\n")
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Kilometers per hour to Miles per hour")
                        print("2. Miles per hour to Kilometers per hour")
                        print("3. Meters per second to Kilometers per hour")
                        print("4. Kilometers per hour to Meters per second")
                        print("5. Back to Main Menu")

                        try:
                            num_of_speed_conversions = int(input("\nPlease enter the number of speed conversions you want to perform (1-5): "))
                            print()
                            if num_of_speed_conversions < 1 or num_of_speed_conversions > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue

                            elif num_of_speed_conversions == 1:
                                print("You have chosen to convert Kilometers per hour to Miles per hour.\n")
                                print("PLEASE NOTE THAT : 1 km/h = 0.621371 mph\n")
                                while True:
                                    try:
                                        kmph = float(input("Please enter the speed in Kilometers per hour: "))
                                        mph = kmph * 0.621371
                                        print("\n" + str(kmph) + " km/h = " + str(mph) + " mph.\n")
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

                            elif num_of_speed_conversions == 2:
                                print("You have chosen to convert Miles per hour to Kilometers per hour.\n")
                                print("PLEASE NOTE THAT : 1 mph = 1.60934 km/h\n")
                                while True:
                                    try:
                                        mph = float(input("Please enter the speed in Miles per hour: "))
                                        kmph = mph * 1.60934
                                        print("\n" + str(mph) + " mph = " + str(kmph) + " km/h.\n")
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

                            elif num_of_speed_conversions == 3:
                                print("You have chosen to convert Meters per second to Kilometers per hour.\n")
                                print("PLEASE NOTE THAT : 1 m/s = 3.6 km/h\n")
                                while True:
                                    try:
                                        mps = float(input("Please enter the speed in Meters per second: "))
                                        kmph = mps * 3.6
                                        print("\n" + str(mps) + " m/s = " + str(kmph) + " km/h.\n")
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

                            elif num_of_speed_conversions == 4:
                                print("You have chosen to convert Kilometers per hour to Meters per second.\n")
                                print("PLEASE NOTE THAT : 1 km/h = 0.277778 m/s\n")
                                while True:
                                    try:
                                        kmph = float(input("Please enter the speed in Kilometers per hour: "))
                                        mps = kmph * 0.277778
                                        print("\n" + str(kmph) + " km/h = " + str(mps) + " m/s.\n")
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

                            elif num_of_speed_conversions == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break

                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue

                elif number_of_conversions == 7:
                    print("\nYou have chosen to perform TIME conversions.\n")
                    while True:
                        print("You can convert between the following units:")
                        print("\n1. Hours to Minutes")
                        print("2. Minutes to Hours")
                        print("3. Minutes to Seconds")
                        print("4. Seconds to Minutes")
                        print("5. Back to Main Menu")

                        try:
                            num_of_time_conversions = int(input("\nPlease enter the number of time conversions you want to perform (1-5): "))
                            print()
                            if num_of_time_conversions < 1 or num_of_time_conversions > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue

                            elif num_of_time_conversions == 1:
                                print("You have chosen to convert Hours to Minutes.\n")
                                print("PLEASE NOTE THAT : 1 hour = 60 minutes\n")
                                while True:
                                    try:
                                        hours = float(input("Please enter the time in Hours: "))
                                        minutes = hours * 60
                                        print("\n" + str(hours) + " hours = " + str(minutes) + " minutes.\n")
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

                            elif num_of_time_conversions == 2:
                                print("You have chosen to convert Minutes to Hours.\n")
                                print("PLEASE NOTE THAT : 1 minute = 0.0166667 hours\n")
                                while True:
                                    try:
                                        minutes = float(input("Please enter the time in Minutes: "))
                                        hours = minutes / 60
                                        print("\n" + str(minutes) + " minutes = " + str(hours) + " hours.\n")
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

                            elif num_of_time_conversions == 3:
                                print("You have chosen to convert Minutes to Seconds.\n")
                                print("PLEASE NOTE THAT : 1 minute = 60 seconds\n")
                                while True:
                                    try:
                                        minutes = float(input("Please enter the time in Minutes: "))
                                        seconds = minutes * 60
                                        print("\n" + str(minutes) + " minutes = " + str(seconds) + " seconds.\n")
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

                            elif num_of_time_conversions == 4:
                                print("You have chosen to convert Seconds to Minutes.\n")
                                print("PLEASE NOTE THAT : 1 second = 0.0166667 minutes\n")
                                while True:
                                    try:
                                        seconds = float(input("Please enter the time in Seconds: "))
                                        minutes = seconds / 60
                                        print("\n" + str(seconds) + " seconds = " + str(minutes) + " minutes.\n")
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

                            elif num_of_time_conversions == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break

                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue
                elif number_of_conversions == 8:
                    print("\nYou have chosen to perform CURRENCY conversions.\n")
                    while True:
                        print("You can convert between the following currencies:")
                        print("\n1. MYR to USD")
                        print("2. USD to MYR")
                        print("3. MYR to RMB")
                        print("4. RMB to MYR")
                        print("5. Back to Main Menu")

                        try:
                            currency_conversion_choice = int(input("\nPlease enter the number of currency conversions you want to perform (1-5): "))
                            print()
                            if currency_conversion_choice < 1 or currency_conversion_choice > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue

                            elif currency_conversion_choice == 1:
                                print("You have chosen to convert MYR to USD.\n")
                                print("PLEASE NOTE THAT: 1 MYR ≈ 0.21 USD (example rate, you may update it based on the latest rate)\n")
                                while True:
                                    try:
                                        myr = float(input("Please enter the amount in MYR: "))
                                        usd = myr * 0.21
                                        print("\n" + str(myr) + " MYR = " + str(usd) + " USD.\n")
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

                            elif currency_conversion_choice == 2:
                                print("You have chosen to convert USD to MYR.\n")
                                print("PLEASE NOTE THAT: 1 USD ≈ 4.75 MYR (example rate, update as needed)\n")
                                while True:
                                    try:
                                        usd = float(input("Please enter the amount in USD: "))
                                        myr = usd * 4.75
                                        print("\n" + str(usd) + " USD = " + str(myr) + " MYR.\n")
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

                            elif currency_conversion_choice == 3:
                                print("You have chosen to convert MYR to RMB.\n")
                                print("PLEASE NOTE THAT: 1 MYR ≈ 1.54 RMB (example rate, update as needed)\n")
                                while True:
                                    try:
                                        myr = float(input("Please enter the amount in MYR: "))
                                        rmb = myr * 1.54
                                        print("\n" + str(myr) + " MYR = " + str(rmb) + " RMB.\n")
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

                            elif currency_conversion_choice == 4:
                                print("You have chosen to convert RMB to MYR.\n")
                                print("PLEASE NOTE THAT: 1 RMB ≈ 0.65 MYR (example rate, update as needed)\n")
                                while True:
                                    try:
                                        rmb = float(input("Please enter the amount in RMB: "))
                                        myr = rmb * 0.65
                                        print("\n" + str(rmb) + " RMB = " + str(myr) + " MYR.\n")
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

                            elif currency_conversion_choice == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break

                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue

                elif number_of_conversions == 9:
                    print("\nYou have chosen to perform ENERGY conversions.\n")
                    while True:
                        print("You can convert between the following energy units:")
                        print("\n1. Joules to Calories")
                        print("2. Calories to Joules")
                        print("3. Joules to Kilowatt-hours")
                        print("4. Kilowatt-hours to Joules")
                        print("5. Back to Main Menu")

                        try:
                            energy_conversion_choice = int(input("\nPlease enter the number of energy conversions you want to perform (1-5): "))
                            print()
                            if energy_conversion_choice < 1 or energy_conversion_choice > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue

                            elif energy_conversion_choice == 1:
                                print("You have chosen to convert Joules to Calories.\n")
                                print("NOTE: 1 Joule ≈ 0.239006 Calories (small calories)\n")
                                while True:
                                    try:
                                        joules = float(input("Please enter the amount in Joules: "))
                                        calories = joules * 0.239006
                                        print("\n" + str(joules) + " Joules = " + str(calories) + " Calories.\n")
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

                            elif energy_conversion_choice == 2:
                                print("You have chosen to convert Calories to Joules.\n")
                                print("NOTE: 1 Calorie ≈ 4.184 Joules\n")
                                while True:
                                    try:
                                        calories = float(input("Please enter the amount in Calories: "))
                                        joules = calories * 4.184
                                        print("\n" + str(calories) + " Calories = " + str(joules) + " Joules.\n")
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

                            elif energy_conversion_choice == 3:
                                print("You have chosen to convert Joules to Kilowatt-hours.\n")
                                print("NOTE: 1 Joules = 0.0000002777778 Kilowatt-hour\n")
                                while True:
                                    try:
                                        joules = float(input("Please enter the amount in Joules: "))
                                        kwh = joules / 3600000
                                        print("\n" + str(joules) + " Joules = " + str(kwh) + " Kilowatt-hours.\n")
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

                            elif energy_conversion_choice == 4:
                                print("You have chosen to convert Kilowatt-hours to Joules.\n")
                                print("NOTE: 1 Kilowatt-hour = 3,600,000 Joules\n")
                                while True:
                                    try:
                                        kwh = float(input("Please enter the amount in Kilowatt-hours: "))
                                        joules = kwh * 3600000
                                        print("\n" + str(kwh) + " Kilowatt-hours = " + str(joules) + " Joules.\n")
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

                            elif energy_conversion_choice == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break

                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue

                elif number_of_conversions == 10:
                    print("\nYou have chosen to perform POWER conversions.\n")
                    while True:
                        print("You can convert between the following power units:")
                        print("\n1. Watts to Kilowatts")
                        print("2. Kilowatts to Watts")
                        print("3. Horsepower to Watts")
                        print("4. Watts to Horsepower")
                        print("5. Back to Main Menu")

                        try:
                            power_conversion_choice = int(input("\nPlease enter the number of power conversions you want to perform (1-5): "))
                            print()
                            if power_conversion_choice < 1 or power_conversion_choice > 5:
                                print("Invalid input. Please enter a number between 1 and 5.\n")
                                continue

                            elif power_conversion_choice == 1:
                                print("You have chosen to convert Watts to Kilowatts.\n")
                                print("NOTE: 1 Watt = 0.001 Killowatt\n")
                                while True:
                                    try:
                                        watts = float(input("Please enter the amount in Watts: "))
                                        kilowatts = watts / 1000
                                        print("\n" + str(watts) + " Watts = " + str(kilowatts) + " Kilowatts.\n")
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

                            elif power_conversion_choice == 2:
                                print("You have chosen to convert Kilowatts to Watts.\n")
                                print("NOTE: 1 Kilowatt = 1000 Watts\n")
                                while True:
                                    try:
                                        kilowatts = float(input("Please enter the amount in Kilowatts: "))
                                        watts = kilowatts * 1000
                                        print("\n" + str(kilowatts) + " Kilowatts = " + str(watts) + " Watts.\n")
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

                            elif power_conversion_choice == 3:
                                print("You have chosen to convert Horsepower to Watts.\n")
                                print("NOTE: 1 Horsepower ≈ 745.7 Watts\n")
                                while True:
                                    try:
                                        hp = float(input("Please enter the amount in Horsepower: "))
                                        watts = hp * 745.7
                                        print("\n" + str(hp) + " Horsepower = " + str(watts) + " Watts.\n")
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

                            elif power_conversion_choice == 4:
                                print("You have chosen to convert Watts to Horsepower.\n")
                                print("NOTE: 1 Watt ≈ 0.001341 Horsepower\n")
                                while True:
                                    try:
                                        watts = float(input("Please enter the amount in Watts: "))
                                        hp = watts / 745.7
                                        print("\n" + str(watts) + " Watts = " + str(hp) + " Horsepower.\n")
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

                            elif power_conversion_choice == 5:
                                print("You have chosen to go back to the main menu.\n")
                                break

                        except ValueError:
                            print("\nInvalid input. Please enter a number between 1 and 5.\n")
                            continue

                elif number_of_conversions == 11:
                    print("\nYou have chosen to quit the program.\n")
                    print("Thank you for using the Basic Unit Converter!\n")
                    print("Goodbye!")
                    exit()

            except ValueError:
                print("\nInvalid input. Please try again and enter a number between 1 and 11.\n")
                continue
