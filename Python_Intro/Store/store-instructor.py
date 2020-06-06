class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


    def adjustPrice(self, increase):
        self.price += self.price * increase

class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, name, price, category):
        product = Product(name, price, category)
        key = product.name
        # print(type(product), "<-- this is the product type")
        # print(type(self.products), "<--- safeway's products type")
        self.products[key] = product
        # print(self.name)
        # # print(self.products[0])

    def increaseProdPrice(self, product_name, increase):
        self.products[product_name].adjustPrice(increase)

myStore = Store("Safeway")
myStore.add_product("banana", 1, "fruits")
# myStore.add_product("basketball", 1, "sporting goods")
# myStore.add_product(productList["broccoli"].name, productList["broccoli"].price, productList["broccoli"].category)

store2 = Store("Target")
store2.add_product("banana", 40, "fruits")


store2.increaseProdPrice("banana", 0.1)
print(store2.products["banana"].price)
print(myStore.products["banana"].price)