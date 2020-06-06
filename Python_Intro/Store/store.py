class Store:
    def __init__(self, storename):
        self.sname = storename
        self.pdlist = []

    def add_product(self, new_product): # takes a product and adds it to the store
        self.pdlist.append(new_product)

    def sell_product(self, id): # remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info
        delpd = self.pdlist[id]
        del self.pdlist[id]
        Product.print_info(delpd)

    def inflation(self, percent_increase): #increases the price of each product by the percent_increase given
        for item in self.pdlist:
            Product.update_price(item, percent_increase, True)

    def set_clearance(self, category, percent_discount): #updates all the products matching the given category by reducing the price by the percent_discount given
        for item in self.pdlist:
            if item.Product.category == category:
                Product.update_price(item, percent_discount, False)



class Product:
    def __init__(self, pdname, price, category, pid):
        self.pname = pdname
        self.price = price
        self.category = category
        self.pid = pid


    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1+percent_change)
        else:
            self.price *= (1-percent_change)

    def print_info(self):
        print(f"************************************\nProduct Name: {self.pname}\nProduct Category: {self.category}\nProduct Price: {self.price}")


Store1=Store('Store1')
Store2=Store('Store2')

Product1=Product('Product1',5,'Beverage',1)
Product2=Product('Product2',10,'Produce',2)
Product3=Product('Product3',100,'Electronics',3)
Product4=Product('Product4',300,'Electronics',4)
Product5=Product('Product5',1000,'Appliance',5)

Store1.add_product(Product1)
Store1.add_product(Product4)
Store1.add_product(Product5)

Store2.add_product(Product2)
Store2.add_product(Product3)
Store2.add_product(Product4)

Store1.sell_product(2)

Store1.inflation(0.015)

Store2.sell_product(2)





