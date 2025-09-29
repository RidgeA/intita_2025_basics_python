# product = {
# 	"name": "Laptop",
# 	"price": 25000,
# 	"quantity": 5,
# 	"category": "Electronics",
# }

# print(f"Product: {product['name']}, price: {product['price']} UAH, quantity: {product['quantity']}, category: {product['category']}")

# product = ("Laptop", 25000, 5, "Electronics")
# print(f"Product: {product[0]}, price: {product[1]} UAH, quantity: {product[2]}, category: {product[3]}")

# example of a product using class
class Product:

    tax_rate = 0.2

    CURRENCY = "UAH"

    def __init__(self, name, price, quantity, category):
        # initialize product attributes
        self.name = name
        self._price = price
        self.__quantity = quantity
        self.category = category
        self.rating = 5
        # print("new product created")

    def print_info(self):
        print(self)

    def __str__(self):
        return f"Product: {self.name}, Price with tax: {self._price + self._price * self.tax_rate} {Product.CURRENCY}, Quantity: {self.__quantity}, Category: {self.category}"

    def __repr__(self):
        return f"Product('{self.name}', {self._price}, {self.__quantity}, '{self.category}')"

    def set_price(self, price):
        if price < 0:
            print("price cannot be below 0")
            return
        
        self._price = price

    def get_price(self):
        return self._price


# create an instance of Product
laptop = Product("Laptop", 25000, 5, "Electronics")
phone = Product("smartphone", 10000, 5, "Electronics")

laptop.print_info()
phone.print_info()

Product.tax_rate = 0.3

laptop.print_info()
phone.print_info()

laptop.tax_rate = 0.1

laptop.print_info()
phone.print_info()


laptop.set_price(-100)
laptop.print_info()

laptop._price = -100
laptop.print_info()

print("=============================")

laptop._Product__quantity = 100
laptop.print_info()

print(phone)

print(repr(phone))
print(repr((1, 2, 3)))

phone2 = eval(repr(phone))
print(phone2)

# print product attributes