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

profit = 0


def is_resources_eff(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print("cant make it")
            return False
    return True


def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters do you have?: ")) * .25
    total += int(input("How many dimes do you have?: ")) * .1
    total += int(input("How many nickles do you have?: ")) * .05
    total += int(input("How many pennies do you have?: ")) * .01
    return total


def afford(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"change back is: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough, money refunded !")
        return False


def make_coffee(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
    print(f"Here is your drink {drink_name}")




machine_asking = True
while machine_asking:

    user_choice = input("What would you like? : ")
    if user_choice == "off":
         machine_asking = False
    elif user_choice == "report":
         w = resources["water"]
         mlk = resources["milk"]
         cof = resources["coffee"]
         print(f"water = {w}, milk = {mlk}, coffee = {cof}, money = {profit}")
    else:
         drink = MENU[user_choice]
         if is_resources_eff(drink["ingredients"]):
             payment = process_coins()
             if afford(payment,drink["cost"]):
                 make_coffee(user_choice, drink["ingredients"])








