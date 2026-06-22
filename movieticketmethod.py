class MovieTicket:
    def __init__(self,movie_name,ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        
    def add_tax(self,percent):
        tax_amount = self.ticket_price * percent / 100
        self.ticket_price += tax_amount
        
    def show_price(self):
        print("Movie name: ", self.movie_name)
        print("Ticket price: ", self.ticket_price)
        
movie_name = input("Enter movie name: ")
ticket_price = int(input("Enter ticket price: "))
m1=MovieTicket(movie_name,ticket_price)
tax_percent=int(input("Enter the tax percentage: "))
m1.add_tax(tax_percent)
m1.show_price()
