Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 210,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 350,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}


def resource_sufficient(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry, There is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert money")
    total = int(input("How many money? : "))
    return total


def transaction_successful(money_received, drink_cost):
    global money
    if money_received >= drink_cost:
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(change)
        money += drink_cost
        return True
    else:
        print("Sorry, That's not enough money. \nMoney Refunded")
        return False


def coffee(drink_name, order):
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name}, Enjoy!!!")


money = 0
on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if choice == 'off':
        on = False
    elif choice == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : Rs. {money}")
    else:
        drink = Menu[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                coffee(choice, drink['ingredients'])
