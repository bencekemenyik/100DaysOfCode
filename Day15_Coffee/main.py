MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(coffee_name):
    water_cost = MENU[coffee_name]["ingredients"]["water"]
    milk_cost = MENU[coffee_name]["ingredients"]["milk"]
    coffee_cost = MENU[coffee_name]["ingredients"]["coffee"]
    if water_cost > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    if milk_cost > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    if coffee_cost > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    return True


def coin_processor(coffee_type):
    coffee_cost = MENU[coffee_type]["cost"]
    print("Please insert coins.")
    nr_quarters = int(input("How many quarters?: "))  # 0.25
    nr_dimes = int(input("How many dimes?: "))  # 0.10
    nr_nickles = int(input("How many nickles?: "))  # 0.05
    nr_pennies = int(input("How many pennies?: "))  # 0.01
    total = nr_quarters * 0.25 + nr_dimes * 0.10 + nr_nickles * 0.05 + nr_pennies * 0.01
    if total < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round(total-coffee_cost,2)} in change.")
        print(f"Here is your {coffee_type} ☕. Enjoy!")
        return True



def coffee_machine():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "off":
        return
    elif coffee_type == "report":
        print_report()
        coffee_machine()
    else:
        if check_resources(coffee_type):
            if coin_processor(coffee_type):
                resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
                resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
                resources["money"] += MENU[coffee_type]["cost"]
                coffee_machine()
            else:
                coffee_machine()
        else:
            coffee_machine()


coffee_machine()

