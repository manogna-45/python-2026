class ShoppingCart:
    def __init__(self,item_name,price):
        self.item_name = item_name
        self.price = price
        
    def discount(self,percent):
        discount_amount = self.price * percent / 100
        self.price -= discount_amount
    def show_price(self):
        print("Item_name: ", self.item_name)
        print("Price: ", self.price)
          
item_name = input("Enter item name: ")
price = int(input("Enter price: "))
sh1=ShoppingCart(item_name, price)

discount_per = int(input("Enter discount percentage: "))
sh1.discount(discount_per)
sh1.show_price()
