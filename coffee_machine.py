class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.waterAmount = water
        self.milkAmount = milk
        self.beansAmount = beans
        self.cupsAmount = cups
        self.moneyAmount = money

    def espresso(self):
        water, milk, beans = 250, 0, 16
        if self.can_do(water, milk, beans):
            self.waterAmount -= water
            self.beansAmount -= beans
            self.cupsAmount -= 1
            self.moneyAmount += 4

    def latte(self):
        water, milk, beans = 350, 75, 20
        if self.can_do(water, milk, beans):
            self.waterAmount -= water
            self.milkAmount -= milk
            self.beansAmount -= beans
            self.cupsAmount -= 1
            self.moneyAmount += 7

    def cappuccino(self):
        water, milk, beans = 200, 100, 12
        if self.can_do(water, milk, beans):
            self.waterAmount -= water
            self.milkAmount -= milk
            self.beansAmount -= beans
            self.cupsAmount -= 1
            self.moneyAmount += 6

    def remaining(self):
        print('')
        print('The coffee machine has: ')
        print(f'{self.waterAmount} of water')
        print(f'{self.milkAmount} of milk')
        print(f'{self.beansAmount} of coffee beans')
        print(f'{self.cupsAmount} of disposable cups')
        print(f'${self.moneyAmount} of money')
        print('')

    def fill(self):
        water = int(input('Write how many ml of water do you want to add: '))
        milk = int(input('Write how many ml of milk do you want to add: '))
        beans = int(
            input('Write how many grams of coffee do you want to add: '))
        cups = int(
            input('Write how many disposable cups of coffee do you want '
                  'to add: '))
        print('')
        self.waterAmount += water
        self.milkAmount += milk
        self.beansAmount += beans
        self.cupsAmount += cups

    def buy(self):
        type_coffee = {'1': self.espresso, '2': self.latte,
                       '3': self.cappuccino}
        option = input('What do you want to buy/ 1- espresso, 2- latte, '
                       '3 - cappuccino, back - to main menu: ')
        if option != 'back':
            func = type_coffee[option]
            func()

    def take(self):
        print(f'I gave you ${self.moneyAmount}\n')
        self.moneyAmount = 0

    def can_do(self, water, milk, beans):
        if water <= self.waterAmount and milk <= self.milkAmount and beans <= \
                self.beansAmount and self.cupsAmount > 0:
            print("I have enough resources, making you a coffee!\n")
            return True
        if water > self.waterAmount:
            print("Sorry, not enough water!\n")
        if milk > self.milkAmount:
            print("Sorry, not enough milk!\n")
        if beans > self.beansAmount:
            print("Sorry, not enough coffee beans!\n")
        if self.cupsAmount < 1:
            print("Sorry, not enough disposable cups!\n")
        return False


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
actions = {'buy': coffee_machine.buy, 'fill': coffee_machine.fill,
           'take': coffee_machine.take, 'remaining': coffee_machine.remaining}

while True:
    action = input('Write action (buy, fill, take, remaining): ')

    if action == 'exit':
        break
    else:
        actions[action]()
