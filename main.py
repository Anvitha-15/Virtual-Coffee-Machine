from data import MENU
from logo import logo

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1 Ask user, what would they like to have or current report of resources in a repeated manner!
is_machine_on = True
profit = 0


def is_resource_sufficient(order_ingredients):  # argument is been passed as an dictionary
    for item in order_ingredients:  # this step loops through each item like water, milk, in dict
        # print(f"{item}: {order_ingredients[item]}")
        if order_ingredients[item] >= resources[item]:  # this step checks the value in order_ingedirent and resources is sufficient
            print(f"Sorry there is no enough {item}")
            return False  # return false when if condition becomes true
    return True  # return true when if condition is false and loop ends



def process_coins():
    print("Please insert coins!")
    total = int(input("How many 1 rupees?    : ")) * 1
    total += int(input("How many 2 rupees?   : ")) * 2
    total += int(input("How many 5 rupees?   : ")) * 5
    total += int(input("How many 10 rupees?  : ")) * 10
    return total



def is_transaction_successfull(money_received, drink_cost):
    """Return true when the payment is accepted, or false"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change} rupees")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry no enough Money for this drink, and your Money is refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """reduces te ingredients from resource from order and prints the coffee name"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕, enjoy your drink!!!")



## 👆 all the functions 👇 while loop starts



while is_machine_on:
    print(logo)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

    elif user_choice == 'off':
        is_machine_on = False


    # TODO: 2 To get the coffee type from user and check whether sufficient resource is available
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            print(f"Cost of {user_choice} is {drink['cost']} rupees!")
            user_payment = process_coins()
            if is_transaction_successfull(user_payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
