print("Welcome to the ATM")
pin_number = 123456

while True:
    attempts = 0

    while attempts < 3:
        try:
            print()  # Blank line for spacing
            insert_pin = int(input("Please enter your ATM pin number (eg:000000): "))

            if insert_pin == pin_number:
                print("\nYou have successfully logged in.\n")

                while True:
                    print("Please select a transaction type:")
                    print("1. Withdraw Money")
                    print("2. Check Balance")
                    print("3. Exit")
                    print()

                    try:
                        transaction_type = int(input("Enter your choice (1-3): "))
                        print()

                        if transaction_type == 1:
                            print("You have selected to withdraw money.")
                            print("Please note that you are only allowed to withdraw in multiples of $50 and only up to 3 attempts per session.")
                            print()

                            # Prompt the user to enter the amount they want to withdraw
                            for attemp in range(3):
                                try:
                                    withdraw_amount = int(input("Enter the amount you want to withdraw: $"))

                                    if withdraw_amount % 50 == 0 and withdraw_amount > 0:
                                        print("\nYou have successfully withdrawn $" + str(withdraw_amount) + ".")
                                        print("Please take your cash.")
                                        print("You will be redirected to the main menu.\n")
                                        break  # Exit after successful withdrawal
                                    else:
                                        print("Invalid withdrawal amount. Please try again.\n")
                                        if attemp == 2:
                                            print("You have entered the wrong withdrawal amount 3 times. Please try again later.")
                                            print("Redirecting to the main menu...\n")
                                            break
                                except ValueError:
                                    print("Invalid input. Please enter a valid number for the withdrawal amount.\n")

                        elif transaction_type == 2:
                            print("You have selected to check your balance.\n")
                            balance = 1000.00
                            print("Your current balance is: $" + str(balance) + ".")
                            print("You will be redirected to the main menu.\n")
                            continue

                        elif transaction_type == 3:
                            print("You have selected to exit the program.")
                            print("Thank you for using our ATM service!")
                            print("Exiting...\n")
                            exit()

                        else:
                            print("Invalid transaction type. Please enter a number between 1 and 3.\n")

                    except ValueError:
                        print("Invalid input. Please enter a valid number for the transaction type.\n")

            else:
                attempts += 1
                print("Incorrect pin number. Please try again.\n")
                if attempts == 3:
                    print("You have entered the wrong pin number 3 times. Your ATM card is blocked.")
                    print("Please contact your bank for assistance.\n")
                    exit()
                else:
                    continue

        except ValueError:
            attempts += 1
            print("Invalid input. Please enter a valid pin number.\n")
            if attempts == 3:
                print("You have entered the wrong pin number 3 times. Your ATM card is blocked.")
                print("Please contact your bank for assistance.\n")
                exit()
