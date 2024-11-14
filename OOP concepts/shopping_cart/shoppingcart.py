class Product:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = {}
        self.quantities = {}
    
    def add_product(self, product,quantity=1):
        if product.name in self.products:
            self.quantities[product.name] += quantity
        else:
            self.products[product.name]=product.price
            self.quantities[product.name] = quantity
        print('Added {quantity} items of  product: {product.name}')

    def remove_product(self, product_name):
        if product_name in self:
            del self.products[product_name]
            del self.quantities[product_name]
            print(f"Product {product_name} added to cart ")
        print("Product not in cart")

    def calculate_total(self ):
        return sum(self.products[name] * quantity for name, quantity in self.quantities.items())

    def show_cart(self):
        if not self.products:
            print("Your cart is empty")

        print("Cart:")
        for name,price in self.products.items():
            quantity = self.quantities[name]
            print (f"Name: {name} : price: {price} x {quantity}")
        print (f"Total Cost: {self.calculate_total()}")

if __name__ == "__main__":
    laptop = Product("Laptop", 1200)
    watch = Product("Watch", 450)

    cart = Cart()
    cart.add_product(laptop, 2)
    cart.add_product(watch, 3)
    cart.calculate_total()
    cart.show_cart()
 

    
    




        


