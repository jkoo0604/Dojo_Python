import store2

class Store:
    def __init__(self, storename):
        self.sname = storename
        self.pdlist = []

    def add_product(self, new_product): # takes a product and adds it to the store
        self.pdlist.append(new_product)

    def sell_product(self, id): # remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info
        delpd = self.pdlist[id]
        del self.pdlist[id]
        store2.Product.print_info(delpd)

    def inflation(self, percent_increase): #increases the price of each product by the percent_increase given
        for item in self.pdlist:
            store2.Product.update_price(item, percent_increase, True)

    def set_clearance(self, category, percent_discount): #updates all the products matching the given category by reducing the price by the percent_discount given
        for item in self.pdlist:
            if item.Product.category == category:
                store2.Product.update_price(item, percent_discount, False)
