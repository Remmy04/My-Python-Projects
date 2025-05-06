print("Welcome to the Bill Tax Tips Calculation program!\n")
print("This program will help you calculate the total bill amount including tax and tips.\n") 

while True:
    try:
        # Get the bill amount from the user
        original_bill = float(input("Please enter your bill amount : $"))
        if original_bill < 0:
            print("\nInvalid bill amount. Please enter a positive number.\n")
            continue
        elif original_bill == 0:
            print("\nThe bill is empty. No tax or tips to calculate.\n")
            print("Thanks for using the Bill Tax Tips Calculation program!\n")
            print("Exiting the program.\n")
            break
        else:
            while True:
                try:
                    # Get the tax rate from the user
                    tax_rate = float(input("\nPlease enter the tax rate (in percentage) : "))
                    if tax_rate < 0:
                        print("\nInvalid tax rate. Please enter a positive number.")
                        continue
                    elif tax_rate == 0:
                        print("\nNo tax to calculate.")
                        tax_amount = 0
                        after_tax_bill = original_bill
                    else:
                        # Calculate the tax amount
                        tax_amount = tax_rate * original_bill / 100
                        after_tax_bill = tax_amount + original_bill
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    continue
                    
                while True:
                    try:
                        # Get the tip percentage from the user
                        tip_percentage = float(input("\nPlease enter the tip percentage (in percentage) : "))
                        if tip_percentage < 0:
                            print("\nInvalid tip percentage. Please enter a positive number.")
                            continue
                        elif tip_percentage == 0:
                            print("\nNo tips to calculate.")
                            tip_amount = 0
                            # If no tip is given, the total bill is the after-tax bill
                            total_bill = after_tax_bill
                            
                        else:
                            # Calculate the tip amount
                            tip_amount = tip_percentage * after_tax_bill / 100
                            total_bill = after_tax_bill + tip_amount
                            
                    except ValueError:
                        print("\nInvalid input. Please enter a valid number.")
                        continue

                    print()   
                    print("The original bill is $" + str(original_bill))
                    print("The tax amount of the bill is $" + str(tax_amount))
                    print("The tip amount of the bill is $" + str(tip_amount))
                    print()
                    print("The TOTAL bill amount is $" + str(total_bill))
                    print()
                    print("Thank you for using the Bill Tax Tips Calculation program!")
                    break
                break

    except ValueError:
        print("\nInvalid input. Please enter a valid number.\n")
        continue

    choice = input("\nDo you want to calculate another bill? (yes/no): ")
    if choice.lower() != 'yes':
        print("\nThank you for using the Bill Tax Tips Calculation program!")
        print("\nExiting the program.\n")
        break
    else:
        print("\nLet's calculate another bill!\n")
        continue