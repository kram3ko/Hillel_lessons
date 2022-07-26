class Product:
    def __init__(self, name, color, price, amount, discount: float = 0):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: price: {self.price} | {self.amount}, discount: {self.discount}%"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def get_price(self):
        return f'Price with discount:{self.name} = {self.price - self.price * (self.discount / 100)}'


class Phone(Product):
    def __init__(self, name, color, price, amount, discount: float, lte=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = " LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional

        return message


class Laptop(Product):
    def __init__(self, name, color, price, amount, discount: float, motherboard_type, material):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material

    def get_product_description(self):
        show_info = f" motherboard: {self.motherboard_type} material: {self.material}"
        msg = super().get_product_description()
        msg += show_info
        return msg


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount=13)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, discount=17, lte=True)
samsung = Phone(name="Samsung S20FE", color="aqua blue", price=16000, amount=4, discount=21, lte=True)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, discount=20, motherboard_type="MSI MPG Z690",
                material='carbon')
asus = Laptop(name="Asus", color="purple", price=3000, amount=6, discount=33, motherboard_type="Gigabyte Z690",
              material="aluminium")
asus_g2 = Laptop("Asus_g2", "grey", 700, 2, 0, "Gigabyte Z690", "plastic")

iphone13.show_description()
iphone7.show_description()
samsung.show_description()
lenovo.show_description()
asus.show_description()
asus_g2.show_description()

if __name__ == "__main__":
    product_list = [iphone7, iphone13, samsung, lenovo, asus, asus_g2]
    for sell_price in product_list:
        print(sell_price.get_price())
