menu_pay = {"dhosa": "100",
            "idli": "90",
            "paratha": "60",
            "roti": "30",
            "pizza": "150",
            "pasta": "130",
            "puri": "20",
            "kaju masala": "100",
            "vadapav": "25"}
menu = ["dhosa",
        "idli",
        "paratha",
        "roti",
        "pizza",
        "pasta",
        "puri",
        "kaju masala",
        "vadapav"]

yes_no = ["Y", "N"]

pay = ["Googlepay", "PayTM", "PhonePay"]

credit_card = ["credit card"]

cash_on_delivery = ["cash on delivery"]

i = 0
print("Welcome to !ZOMATO! Your favourite online food delivery company")
print("PLease order your meal through menu\n\n")

while (1):
    print("Menu:\n")
    print(menu_pay,"\t")



    food = input("Please enter item you want to eat\n")

    print("You have to pay -/",menu_pay.__getitem__(food),"for",food)

    if food in menu:
        print("payment option:\n(1)cash on delivery\n(2)Googlepay\n(3)PayTM\n(4)PhonePay\n(5)credit card")

        payment = input()

        if payment in pay:
            print("Please enter your", payment, "number")

        elif payment == "credit card":
            print("Please enter you your credit card pin")

        elif payment == "cash on delivery":
            print("Give payment to delivery boy")

        else:
            print("Enter a valid payment option")

        amount = input()

        print("Thanks for ordering food from us;\nYour order is placed")

        print("Please enter the location for delivery")

        location = input()

        print("Your item will be delivered to", location, "in 15 minutes")
    else:
        print("PLease enter a valid item (check the menu)")
        continue

    print("""Will you want to order more items enter "Y" if not please enter "N"\n """)

    more = input()

    if more == "Y":
        continue

    elif more == "N":
        print("Have a nice day")
        break

    else:
        print("Enter a valid syntex")
        continue




