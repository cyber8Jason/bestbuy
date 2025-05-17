from xml.dom import VALIDATION_ERR


class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Error: name cant be empty!")
        if price < 0:
            raise ValueError("Price cant be negative")
        if quantity < 0:
            raise ValueError("Quantity cant be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cant be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return product_info


    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity available.")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()