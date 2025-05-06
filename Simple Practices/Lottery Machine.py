import random

while True:
    user_input = input("Please enter 'Q' to quit or any key to continue: ")
    if user_input.upper() == 'Q':
        print("Exiting... Bye!")
        break
    else:
        print("Let's play the lottery!")
        try:
            your_numbers = int(input("Please enter your number (1-20): "))

            if your_numbers < 1 or your_numbers > 20:
                print("Invalid input! Please enter a number between 1 and 20.")
            else:
                machine_numbers = random.randint(1, 20)
                print("Your number is:", your_numbers)
                print("Machine number is:", machine_numbers)

                if your_numbers == machine_numbers:
                    print("🎉 Congratulations! You guessed the number!")
                else:
                    print("❌ Sorry, try again!")

        except ValueError:
            print("Invalid input! Please enter a number, not text.")
        finally:
            print("Thank you for playing!\n")