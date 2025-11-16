

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price



class VendingMachine:
    def __init__(self):
        # the list of drinks
        self.drinks = []
        self.drinks.append(Beverage("Cola", 1.50))
        self.drinks.append(Beverage("Pepsi", 1.25))
        self.drinks.append(Beverage("Water", 1.00))
        self.drinks.append(Beverage("Sprite", 1.30))
        self.drinks.append(Beverage("Fanta", 2.00))
        self.drinks.append(Beverage("Dew", 1.75))

    def showMenu(self):
        print("\nVending Machine Menu:")
        for i in range(len(self.drinks)):
            drink = self.drinks[i]
            print(i + 1, drink.name, "-", "$" + str(drink.price))

    def run(self):
        while True:  # keep on running
            self.showMenu()
            choice = int(input("Select a drink (1-6): "))

            if choice >= 1 and choice <= 6:
                drink = self.drinks[choice - 1]
                print("You selected", drink.name, "Price:", drink.price)
                money = float(input("Insert money: "))

                if money == drink.price:
                    print("Vending...", drink.name)

                elif money > drink.price:
                    change = money - drink.price
                    print("Vending", drink.name, "... Your change is", round(change, 2), "\n")

                else:
                    print("Not enough money. Please insert more.\n")

            else:
                print("Invalid choice.\n")


# made the machine object and keep running
machine = VendingMachine()
machine.run()
