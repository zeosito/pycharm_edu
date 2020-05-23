# cups = int(input("Write how many cups of coffee you will need:\n"))
# water = 200
# milk = 50
# coffe_beans = 15
# print(f"for {cups} of coffee you will need:")
# print(f"{water * cups} ml of water")
# print(f"{milk * cups} ml of milk")
# print (f"{coffe_beans * cups} g of coffee beans")
# water_have = int(input("Write how many ml of water the coffee machine has:\n"))
# milk_have = int(input("Write how many ml of milk the coffee machine has:\n"))
# coffee_beans_have = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
# cups = int(input("Write how many cups of coffee you will need:\n"))

# water_cup_qty = water_have // 200
# milk_cup_qty = milk_have // 50
# coffe_cup_qty = coffee_beans_have // 15
# possibility = [water_cup_qty, milk_cup_qty, coffe_cup_qty]

# if min(possibility) == cups:
#    print(f"Yes, I can make that amount of coffee")
# elif min(possibility) > cups:
#    print(f"Yes, I can make that amount of coffee (and even {min(possibility) - cups} more than that)")
# else:
#    print(f"No, I can make only {min(possibility)} cups of coffee")

money = 550
water = 400
milk = 540
coffe_beans = 120
cups = 9


def print_statements():
    print("The coffee machine has:\n"
          f"{water} of water\n"
          f"{milk} of milk\n"
          f"{coffe_beans} of coffee beans\n"
          f"{cups} of disposable cups\n"
          f"{money} of money\n")


def buy():
    selection = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
    global money, water, coffe_beans, milk, cups
    if selection == "1" and water >= 250:
        money += 4
        water -= 250
        coffe_beans -= 16
        cups -= 1
        print("I have enough resources, making you a coffee!\n")
    elif selection == "2" and water >= 350:
        money += 7
        water -= 350
        milk -= 75
        coffe_beans -= 20
        cups -= 1
        print("I have enough resources, making you a coffee!\n")
    elif selection == "3" and water >= 200:
        money += 6
        water -= 200
        milk -= 100
        coffe_beans -= 12
        cups -= 1
        print("I have enough resources, making you a coffee!\n")
    elif selection == "back":
        return 'back'
    else:
        print("Sorry, not enough water!\n")


def fill():
    global money, water, coffe_beans, milk, cups
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffe_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))


def take():
    global money
    print(f"I gave you ${money}")
    money = 0



action = ""
while action != 'exit':
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'remaining':
        print_statements()
    if action == 'buy':
            buy()
    if action == 'take':
        take()
    if action == 'fill':
        fill()
