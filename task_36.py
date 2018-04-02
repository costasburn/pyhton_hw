import datetime


class Store:
    def __init__(self):
        self.stock = {}
        self.sales_log = {}

    def add_item(self, item_to_add, quantity_to_add):
        if item_to_add in self.stock:
            self.stock[item_to_add] += quantity_to_add
        else:
            self.stock.update({item_to_add: quantity_to_add})
        return self.balance(item=item_to_add)

    def sell_item(self, item_to_sell, quantity_to_sell):
        if self.sales_log:
            self.sales_log[item_to_sell.name] = self.sales_log[item_to_sell.name], (datetime.datetime.now().date(), quantity_to_sell)
        else:
            self.sales_log[item_to_sell.name] = (datetime.datetime.now().date(), quantity_to_sell)

        if item_to_sell in self.stock:
            if quantity_to_sell < self.stock[item_to_sell]:
                self.stock[item_to_sell] -= quantity_to_sell
                print("Quantity of {0}s has been reduced by {1}. "
                      "Now there are {2} {0}s in stock"
                      .format(item_to_sell.name, quantity_to_sell, self.stock[item_to_sell]))
            else:
                self.stock.pop(item_to_sell)
                print("There were only {} {}s in the stock. "
                      "All of them has been removed."
                      .format(self.stock[item_to_sell], item_to_sell))
            return self.balance(item=None)
        else:
            raise ValueError("Requested item ({}) hasn't been found in stock".format(item_to_sell))

    def balance(self, item=None):
        if item in self.stock:
            return print("Currently {}s in stock: {} pcs".format(item.name, self.stock[item]))
        if item is None:
            print("Stock:")
            for item in self.stock:
                print(item.name, ":", self.stock[item])
        else:
            raise ValueError("Requested item ({}) hasn't been found in stock".format(item))


class Item:

    def __init__(self, id, name, description, purchase_price, sell_price):
        self.id = id
        self.name = name
        self.description = description
        self.purchase_price = purchase_price
        self.sell_price = sell_price

    def print_info(self):
        print("Name:            ", self.name)
        print("ID:              ", self.id)
        print("Description:      \"{}\"".format(self.description))
        print("Purchase price:  ", self.purchase_price)
        print("Sell price:      ", self.sell_price)


class Electronics(Item):

    def __init__(self, id, name, description, purchase_price, sell_price, energy_class):
        super().__init__(id, name, description, purchase_price, sell_price)
        self.energy_class = energy_class


class Clothes(Item):

    def __init__(self, id, name, description, purchase_price, sell_price, size):
        super().__init__(id, name, description, purchase_price, sell_price)
        self.size = size


class Foods(Item):

    def __index__(self, id, name, description, purchase_price, sell_price, expiry_date):
        super().__init__(id, name, description, purchase_price, sell_price)
        self.expiry_date = expiry_date


class Report:

    def __init__(self, id):
        self.id = id

    def sales_by_items(self, date1, date2, item):#date parameter must be in datetime.date() format
        amount_of_sold_items = 0
        if date1 and date2 and item:
            for sale in new_store.sales_log[item.name]:
                if date1 < sale[0] < date2:
                    amount_of_sold_items += sale[1]

        return amount_of_sold_items


new_store = Store()

Book = Item(id=1, name="Lord Of The Rings", description="Advanture", purchase_price=10, sell_price=14)
new_store.add_item(Book, 5)
Mobile = Electronics(id=2, name="Nokia", description="8800", purchase_price=200, sell_price=300, energy_class="A1")
new_store.add_item(Mobile, 15)
new_store.balance()
new_store.sell_item(Book, 3)
new_store.sell_item(Book, 1)
new_report = Report(id=1)
print(new_store.sales_log)
print(new_report.sales_by_items(date1=datetime.date(2017, 1, 1),
                                date2=datetime.date(2019, 1, 1),
                                item=Book))
