print("Welcome to the Shopping Discount Program!")
print("This program will help you calculate your total price after applying discounts based on your loyalty level.")

while True:
    user_input = input("Please enter any key to continue or N to exit : ")
    if user_input.lower() == "n":
        print("You have chosen to exit.")
        exit()
    else:
        try:
            total_price = float(input("Please enter the total price : $"))

            # Inner loop to repeatedly ask for loyalty level until valid input is given
            while True:
                loyalty_levels = input("Please enter your loyalty levels (Gold, Silver, Bronze) : ")
                
                if loyalty_levels.lower() == "gold":
                    discount = 0.20
                    if total_price > 500:
                        discount = 0.25
                    break  # Exit the inner loop after valid input
                
                elif loyalty_levels.lower() == "silver":
                    discount = 0.10
                    break  # Exit the inner loop after valid input

                elif loyalty_levels.lower() == "bronze":
                    discount = 0.05
                    break  # Exit the inner loop after valid input

                else:
                    print("Invalid loyalty level. Please enter Gold, Silver, or Bronze.")
                    continue  # Go back to loyalty input only

            price_after_discount = total_price * (1 - discount)
            print("Your total price after discount is : $" + str(price_after_discount) + ".")
            print("Thank you for shopping with us!")

        except ValueError:
            print("Invalid input. Please try again and enter a valid number for the total price.")
        except Exception as e:
            print(f"An error occurred: {e}")