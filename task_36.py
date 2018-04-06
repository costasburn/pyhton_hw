import datetime


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self._stock = {}

    def add_item(self, item_to_add, quantity_to_add):
        if item_to_add in self._stock:
            self._stock[item_to_add] += quantity_to_add
        else:
            self._stock.update({item_to_add: quantity_to_add})
        return self._stock[item_to_add]

    def sell_item(self, item_to_sell, quantity_to_sell):
        if self._stock[item_to_sell] > 0:
            quantity_to_sell = min(quantity_to_sell, self._stock[item_to_sell])
            SaleInvoiceJournal.add_invoice(self, item=item_to_sell, quantity_sold=quantity_to_sell, store=self)
            self._stock[item_to_sell] -= quantity_to_sell
            return self._stock[item_to_sell]
        else:
            Report.not_found(self, item=item_to_sell)
            return False, None

    def balance(self, item=None, balance_time=None):
        if item and balance_time and item in self._stock:
            past_balance = self._stock[item] + Report.sales_by_items(self, filter_item=item, date1=balance_time)
            return past_balance
        if item and not balance_time and item in self._stock:
            Report.print_item(self, store=self, item=item)
            return self._stock[item]
        if item is None:
            return Report.print_stock(self, self._stock)
        else:
            Report.not_found(self, item=item)
            return False, None


class Item:
    _last_id = 0

    def __init__(self, name, description, purchase_price, sell_price):
        Item._last_id += 1
        self.id = Item._last_id
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

    def __init__(self, name, description, purchase_price, sell_price, energy_class):
        super().__init__(name, description, purchase_price, sell_price)
        self.energy_class = energy_class


class Clothes(Item):

    def __init__(self, name, description, purchase_price, sell_price, size):
        super().__init__(name, description, purchase_price, sell_price)
        self.size = size


class Foods(Item):

    def __init__(self, name, description, purchase_price, sell_price, expiry_date):
        super().__init__(name, description, purchase_price, sell_price)
        self.expiry_date = expiry_date


class Report:
    _last_report_id = 0

    def __init__(self):
        Report._last_report_id += 1
        self.id = Report._last_report_id

    # date parameter must be in datetime.date() format
    def sales_by_items(self, filter_item, date1=None, date2=None):

        amount_of_sold_items = 0

        if date1 and date2 and filter_item:
            for invoice in SaleInvoiceJournal.invoices:
                if invoice.item.name == filter_item.name:
                    if date1 < invoice.time_of_invoice < date2:
                        amount_of_sold_items += invoice.quantity_sold
        if date1:
            for invoice in SaleInvoiceJournal.invoices:
                if invoice.item.name == filter_item.name:
                    if date1 < invoice.time_of_invoice:
                        amount_of_sold_items += invoice.quantity_sold
        if date2:
            for invoice in SaleInvoiceJournal.invoices:
                if invoice.item.name == filter_item.name:
                    if invoice.time_of_invoice < date2:
                        amount_of_sold_items += invoice.quantity_sold

        return amount_of_sold_items

    def print_stock(self, stock):
        print()
        print("*" * 20)
        if stock:
            print("Stock:")
            for item in stock:
                print(item.name, ":", stock[item])
        else:
            print("Stock is empty")
        print("*" * 20)

    def print_item(self, store, item):
        print()
        print("*" * 20)
        if store._stock[item]:
            print("Currently {} pcs of {} in stock".format(store._stock[item], item.name))
        else:
            print("Currently no {} in stock".format(item.name))
        print("*" * 20)

    def print_invoice(self, invoices):
        try:
            for invoice in invoices:
                print(
                    "Invoice ID:        {}"
                    "\nTime:            {}"
                    "\nItem:            {}"
                    "\nQuantity sold:   {}".format(invoice.records['ID'], invoice.records['Time'],
                                                   invoice.records['Item'], invoice.records['Quantity']))
                print()
        except TypeError:
            print(
                "Invoice ID:        {}"
                "\nTime:            {}"
                "\nItem:            {}"
                "\nQuantity sold:   {}".format(invoices.records['ID'], invoices.records['Time'],
                                               invoices.records['Item'], invoices.records['Quantity']))
            print()


    def not_found(self, item):
        print("{} was not found in the stock or not enough pcs in stock".format(item.name))


class SaleInvoiceJournal:
    invoices = []
    _last_journal_id = 0

    def __init__(self, journal_name):
        SaleInvoiceJournal._last_journal_id += 1
        self.id = SaleInvoiceJournal._last_journal_id
        self.journal_name = journal_name

    def get_invoices(self, date1=None, date2=None):
        result = []
        print(SaleInvoiceJournal.invoices)
        if date1 and date2:
            for invoice in SaleInvoiceJournal.invoices:
                if date1 < invoice.time_of_invoice.date() < date2:
                    result.append(invoice)
        if date1 and not date2:
            for invoice in SaleInvoiceJournal.invoices:
                if date1 < invoice.time_of_invoice.date():
                    result.append(invoice)
        if date2 and not date1:
            for invoice in SaleInvoiceJournal.invoices:
                if invoice.time_of_invoice.date() < date2:
                    result.append(invoice)
        return result

    def add_invoice(self, item, quantity_sold, store, time_of_invoice_to_add=datetime.datetime.now()):
        balance_before = store.balance(item=item, balance_time=time_of_invoice_to_add)
        if quantity_sold <= balance_before:  # in case the function called by user
            new_invoice = Invoice(time_of_invoice=time_of_invoice_to_add, item=item, quantity_sold=quantity_sold)
            if SaleInvoiceJournal.invoices:
                post_quantity_sold_total = 0
                for invoice in SaleInvoiceJournal.invoices:
                    if invoice.time_of_invoice > time_of_invoice_to_add and item.name == invoice.item.name:
                        post_quantity_sold_single_invoice = invoice.quantity_sold
                        post_quantity_sold_total += post_quantity_sold_single_invoice
                if post_quantity_sold_total > balance_before - quantity_sold:
                    Report.not_found(self, item=item)
                    return False, None
                else:
                    SaleInvoiceJournal.invoices.append(new_invoice)
            else:
                SaleInvoiceJournal.invoices.append(new_invoice)
            return new_invoice
        else:
            Report.not_found(self, item=item)
            return False, None

    def remove_invoice(self, invoice_id):
        for invoice in SaleInvoiceJournal.invoices:
            if invoice.id == invoice_id:
                SaleInvoiceJournal.invoices.remove(invoice)


class Invoice:
    last_invoice_id = 0

    def __init__(self, time_of_invoice, item, quantity_sold):
        self.records = {}
        Invoice.last_invoice_id += 1
        self.id = self.last_invoice_id
        self.time_of_invoice = time_of_invoice
        self.item = item
        self.quantity_sold = quantity_sold
        self.sell_price = item.sell_price
        self.records.update({"ID": self.id, "Time": self.time_of_invoice,
                             "Item": [self.item.name], "Quantity": [self.quantity_sold], "Sell price": [self.sell_price]})

    def add_item_to_invoice(self, item, quantity, store):
        if item in store._stock:
            self.records['Item'].append(item.name)
            self.records['Quantity'].append(quantity)
            self.records['Sell price'].append(item.sell_price)
        else:
            Report.not_found(self, item=item)
            return False, None

    def remove_item_from_invoice(self, item):
        if item.name in self.records['Item']:
            item_index = self.records['Item'].index(item.name)
            self.records['Item'].remove(item.name)
            self.records['Quantity'].remove(self.records['Quantity'][item_index])
            self.records['Sell price'].remove(item.sell_price)
        else:
            Report.not_found(self, item=item)
            return False, None

    def print_info(self, invoices):
        Report.print_invoice(invoices=invoices)


new_store = Store(store_name='Carefour')
new_journal = SaleInvoiceJournal(journal_name="Accountant's journal")
new_report = Report()

Book = Item(name='Lord of the Rings', description='Adventure', purchase_price=12, sell_price=14)
Mobile = Electronics(name='Nokia', description='8800', purchase_price=150, sell_price=200, energy_class='A1')
Milk = Foods(name='Good milk', description='cow milk', purchase_price=4, sell_price=8,
             expiry_date=datetime.date(year=2018, month=4, day=19))

new_store.add_item(item_to_add=Milk, quantity_to_add=10)
new_store.add_item(item_to_add=Book, quantity_to_add=5)
new_store.add_item(item_to_add=Mobile, quantity_to_add=10)

new_store.sell_item(item_to_sell=Book, quantity_to_sell=1)
new_store.sell_item(item_to_sell=Mobile, quantity_to_sell=100)
new_store.sell_item(item_to_sell=Milk, quantity_to_sell=1)
new_store.sell_item(item_to_sell=Milk, quantity_to_sell=1)

new_list_of_invoices = new_journal.get_invoices(date1=datetime.date(2017, 1, 1), date2=datetime.date(2019, 1, 1))
# new_report.print_invoice(invoices=new_list_of_invoices)

new_journal.add_invoice(
    time_of_invoice_to_add=datetime.datetime(year=2018, month=4, day=4, hour=12, minute=30, second=0, microsecond=0),
    item=Book, quantity_sold=1, store=new_store)

# new_list_of_invoices = new_journal.get_invoices(date1=datetime.date(2017, 1, 1), date2=datetime.date(2019, 1, 1))
# new_report.print_invoice(invoices=new_list_of_invoices)

new_journal.remove_invoice(invoice_id=2)

# new_list_of_invoices = new_journal.get_invoices(date1=datetime.date(2017, 1, 1), date2=datetime.date(2019, 1, 1))
# new_report.print_invoice(invoices=new_list_of_invoices)

my_invoice = SaleInvoiceJournal.invoices[2]
new_report.print_invoice(invoices=my_invoice)
my_invoice.add_item_to_invoice(item=Mobile, quantity=2, store=new_store)
new_report.print_invoice(invoices=my_invoice)
my_invoice.remove_item_from_invoice(item=Mobile)
new_report.print_invoice(invoices=my_invoice)
