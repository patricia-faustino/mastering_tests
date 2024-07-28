class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        
class Stock:
    def __init__(self):
        self.products = {}
        
    def add_product(self, product):
        if product.name not in self.products:
            self.products[product.name] = product.quantity
        else:
            self.products[product.name] += product.quantity

            
    def verify_quantity(self, product):
        return self.products.get(product.name, 0)