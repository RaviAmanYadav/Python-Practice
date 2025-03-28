class Menu:
    def __init__(self):
        print("Welcome to the Python Hotel")
        self.menu = {
            "Tea": 10,
            "Coffee": 20,
            "Pizza": 100,
            "burger": 80,
            "Pasta": 60,
        }

    def showMenu(self):
        print("Menu")
        for item, price in self.menu.items():
            print(f"{item} - {price} Rs")


shopMenu = Menu()
shopMenu.showMenu()
