class Lunch:
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if ("menu 1"):
            print("Your choice:", self.menu, "Price 12.00")
        if ("menu 2"):
            print("Your choice:", self.menu, "Price 13.40")
        else:
            print("Error in menu")
Bob = Lunch("menu 1")
Bob.menu_price()