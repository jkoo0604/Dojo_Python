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