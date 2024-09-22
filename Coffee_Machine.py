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

machine = True
PROFIT = 0


def res_sufficient(drink):
    for i in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][i] < resources[i]:
            print("please pay.")
            return True
        else:
            print(f"sorry, there is not enough {i}")
            break


def coins():
    global TOTAL
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickels = int(input("Insert nickels: "))
    pennies = int(input("Insert pennies: "))
    TOTAL = round(quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01, 2)
    print(f"You have paid ${TOTAL}.")


def tran_success(selected):
    global PROFIT
    if TOTAL < MENU[selected]["cost"]:
        print(f"sorry, {TOTAL} is not enough money. Money's refunded.")
    elif TOTAL == MENU[selected]['cost']:
        PROFIT += MENU[selected]["cost"]
        print(f"Enjoy your {selected}")
    else:
        change = TOTAL - MENU[selected]["cost"]
        for i in MENU[selected]['ingredients']:
            resources[i] = resources[i] - MENU[selected]['ingredients'][i]
        PROFIT += MENU[selected]["cost"]
        print(f"Here is your change ${change}. Enjoy your {selected}.")


while machine:
    TOTAL = 0
    choice = input("What would you like? ( espresso / latte / cappuccino ):\n").lower()
    if choice == "off":
        machine = False
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"money : ${PROFIT}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if res_sufficient(choice):
            coins()
            tran_success(choice)
