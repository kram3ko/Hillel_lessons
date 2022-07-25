
class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: price: {self.price} | {self.amount}, discount: {self.discount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def get_price(self):
        print(f'{self.price - self.price * (self.discount / 100)}')


class Phone(Product):
    def __init__(self, name, color, price, amount, discount, lte=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = " LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional

        return message


class Laptop(Product):
    def __init__(self, name, color, price, amount, discount, motherboard_type, socket):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.socket = socket

    def get_product_description(self):
        aditi = f" motherboard: {self.motherboard_type} type socket:{self.socket}"
        msg = super().get_product_description()
        msg += aditi
        return  msg




iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount=13)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, discount=17, lte=True)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, discount=20, motherboard_type="MSI MPG Z690",
                socket=1700)
macbook = Laptop("Gred", "bluemetalic",3000,6,33,"Gigabyte Z690", 1700)


iphone13.show_description()
iphone7.show_description()
lenovo.show_description()
macbook.show_description()
macbook.get_price()