import store1
import store2


Store1=store1.Store('Store1')
Store2=store1.Store('Store2')

Product1=store2.Product('Product1',5,'Beverage',1)
Product2=store2.Product('Product2',10,'Produce',2)
Product3=store2.Product('Product3',100,'Electronics',3)
Product4=store2.Product('Product4',300,'Electronics',4)
Product5=store2.Product('Product5',1000,'Appliance',5)

Store1.add_product(Product1)
Store1.add_product(Product4)
Store1.add_product(Product5)

Store2.add_product(Product2)
Store2.add_product(Product3)
Store2.add_product(Product4)

Store1.sell_product(2)

Store1.inflation(0.015)

Store2.sell_product(2)