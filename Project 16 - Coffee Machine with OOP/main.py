from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem("latte", 200, 150, 24,2.5)
espresso = MenuItem("espresso",50, 0,18, 1.5)
capuccino = MenuItem("cappuccino", 250, 100, 24, 3)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == "off":
        is_on = False
    elif order == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(order)
        if drink:
            enough_resources = coffee_maker.is_resource_sufficient(drink)

            if enough_resources:
                payment_successful = money_machine.make_payment(drink.cost)

                if payment_successful:
                    coffee_maker.make_coffee(drink)