from classes.customer import Customer
from classes.coffee import Coffee

class Order:

    all =[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)

        customer.coffees(self.coffee)
        coffee.customers(self.customer)

        coffee.orders(self)
        customer.orders(self)
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if type(price) == int and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("Invalid price")

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Not a customer object")
        
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Not a coffee object")
