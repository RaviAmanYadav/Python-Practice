from hotelMenu import Menu




class Customer:
    def __init__(self):
        self.customerOrderList = []
        self.totalBill = 0


    def addOrder(self, order, menu):
        if order in menu:
            self.customerOrderList.append(order)
            print(f"{order} is added to your list")
        else:
            print(f"sorry, {order} is not available in the menu")
    
   
    def showCustomerOrders(self):
        print("Your Orders")
        for order in self.customerOrderList:
            print(order)

    def calculateBill(self, menu):
        self.totalBill = sum(menu.menu[item] for item in self.customerOrderList)
        print(f"Your total bill is {self.totalBill} RS")


menu = Menu()


customer = Customer()
while True:
    order = input("\nEnter your order: ").capitalize()
    if order.lower == "done":
        break
    customer.addOrder(order, menu)

customer.showCustomerOrders()
customer.calculateBill(menu)
        


