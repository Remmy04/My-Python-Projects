try: 
    customer_height = int(input("Enter your height in cm: "))
    customer_credit = int(input("Enter your credit: "))

    if customer_height >= 137 and customer_credit >=10:
        print("You can ride the roller coaster!")
    elif customer_height >= 137 and customer_credit < 10:
        print("You don't have enough credit to ride the roller coaster.")
    elif customer_height < 137 and customer_credit >= 10:
        print("You are not tall enough to ride the roller coaster.")
    elif customer_height < 137 and customer_credit < 10:
        print("You are not tall enough and don't have enough credit to ride the roller coaster.")

except ValueError:
    print("Please enter valid numeric values for height and credit.")