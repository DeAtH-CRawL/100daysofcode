"""
A command-line based coffee machine simulator.

This script simulates a coffee machine that can brew three types of coffee: espresso, latte, and cappuccino.
It manages a limited set of resources (water, milk, coffee) and tracks the profit from sales.

The user can:
- Order a coffee by typing its name.
- Turn off the machine by typing 'off'.
- Get a report of the current resources and profit by typing 'report'.

The machine checks for sufficient resources before brewing, processes coin payments,
calculates change, and updates the resource levels after a successful purchase.
"""

# TODO:
# TODO1. Handle invalid drink choices gracefully (e.g., when a user enters a drink not in the MENU).
# TODO2. Add input validation for coins to handle non-numeric input from the user.
# TODO3. Refactor the report logic into its own dedicated function for better organization.
# TODO4. (Advanced) Refactor the code to use a CoffeeMachine class to encapsulate state (resources, profit)
#    and behavior, reducing the reliance on global variables.


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    """Checks if there are sufficient resources to make a drink.

    Args:
        order_ingredients (dict): A dictionary of the required ingredients and their amounts.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Prompts the user to insert coins and returns the total value.

    Returns:
        float: The total value of the coins inserted.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Checks if the payment is sufficient and processes the transaction.

    Args:
        money_received (float): The amount of money received from the user.
        drink_cost (float): The cost of the drink.

    Returns:
        bool: True if the transaction is successful, False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources and serves the drink.

    Args:
        drink_name (str): The name of the drink being made.
        order_ingredients (dict): A dictionary of the required ingredients and their amounts.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

profit = 0



while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
 