import datetime


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self._stock = {}

    def add_item(self, journal, item_to_add, quantity_to_add):
        self._stock[item_to_add] = self._stock.get(item_to_add, 0) + quantity_to_add
        new_log_entry = LogEntry(item=item_to_add, quantity_added=quantity_to_add, time=datetime.datetime.now())
        journal.replenishment_log.append(new_log_entry)
        return self._stock[item_to_add]

    def sell_item(self, journal_for_invoice, item_to_sell, quantity_to_sell):
        if quantity_to_sell <= self._stock[item_to_sell]:
            new_invoice = Invoice(item=item_to_sell, quantity_sold=quantity_to_sell, time_of_invoice=datetime.datetime.now())
            journal_for_invoice.add_invoice(journal_for_invoice, store=self, new_invoice=new_invoice)
            self._stock[item_to_sell] -= quantity_to_sell
            return self._stock[item_to_sell]
        else:
            Report.not_found(self, item=item_to_sell)
            return False, None

    def balance(self, journal, item=None, balance_time=None):
        if item and balance_time and item in self._stock:
            past_balance = self._stock[item] \
                           + Report.sales_by_items(self, journal=journal, filter_item=item, date1=balance_time) \
                           - Report.items_replenished(self, filter_item=item, journal=journal, date1=balance_time)
            return past_balance
        if item and not balance_time and item in self._stock:
            return self._stock[item]
        if item is None:
            return self._stock
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
    def sales_by_items(self, journal, filter_item, date1=None, date2=None):

        amount_of_sold_items = 0

        if date1 and date2 and filter_item:
            for invoice in journal.invoices:
                if invoice.item.name == filter_item.name:
                    if date1 < invoice.time_of_invoice < date2:
                        amount_of_sold_items += invoice.quantity_sold

        if date1 and filter_item and not date2:
            for invoice in journal.invoices:
                if invoice.item.name == filter_item.name:
                    if date1 < invoice.time_of_invoice:
                        amount_of_sold_items += invoice.quantity_sold

        if date2 and filter_item and not date1:
            for invoice in journal.invoices:
                if invoice.item.name == filter_item.name:
                    if invoice.time_of_invoice < date2:
                        amount_of_sold_items += invoice.quantity_sold

        if filter_item and not date1 and not date2:
            for invoice in journal.invoices:
                if invoice.item.name == filter_item.name:
                    amount_of_sold_items += invoice.quantity_sold

        return amount_of_sold_items

    def items_replenished(self, journal, filter_item, date1=None, date2=None):

        amount_of_replenished_items = 0

        if date1 and date2 and filter_item:
            for log_entry in journal.replenishment_log:
                if log_entry.item.name == filter_item.name:
                    if date1 < log_entry.item < date2:
                        amount_of_replenished_items += log_entry.quantity_added

        if date1 and filter_item and not date2:
            for log_entry in journal.replenishment_log:
                if log_entry.item.name == filter_item.name:
                    if date1 < log_entry.time:
                        amount_of_replenished_items += log_entry.quantity_added

        if date2 and filter_item and not date1:
            for log_entry in journal.replenishment_log:
                if log_entry.item.name == filter_item.name:
                    if log_entry.time < date2:
                        amount_of_replenished_items += log_entry.quantity_added

        if filter_item and not date1 and not date2:
            for log_entry in journal.replenishment_log:
                if log_entry.item.name == filter_item.name:
                    amount_of_replenished_items += log_entry.quantity_added

        return amount_of_replenished_items

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
        try:
            print("Currently {} pcs of {} in stock".format(store._stock[item], item.name))
        except KeyError:
            print("Currently no {} in stock".format(item))
        print("*" * 20)

    def print_invoice(self, invoices):
        try:
            print("Invoices:")
            print()
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

    def print_replenishment_log(self, journal):
        print("Replenishment log:")
        for log_entry in journal.replenishment_log:
            print(
                "\nTime:            {}"
                "\nItem:            {}"
                "\nQuantity added:  {}"
                "\nPurchase price:  {}".format(log_entry.records['Time'], log_entry.records['Item'].name,
                                                log_entry.records['Quantity_added'], log_entry.records['Purchase price']))
        print()



    def not_found(self, item):
        print("{} was not found in the stock or not enough pcs in stock".format(item.name))


class SaleInvoiceJournal:
    _last_journal_id = 0

    def __init__(self, journal_name):
        SaleInvoiceJournal._last_journal_id += 1
        self.id = SaleInvoiceJournal._last_journal_id
        self.journal_name = journal_name
        self.invoices = []
        self.replenishment_log = []

    def get_invoices(self, date1=None, date2=None):
        if date1 and date2:
            for invoice in self.invoices:
                if date1 < invoice.time_of_invoice.date() < date2:
                    yield invoice
        if date1 and not date2:
            for invoice in self.invoices:
                if date1 < invoice.time_of_invoice.date():
                    yield invoice
        if date2 and not date1:
            for invoice in self.invoices:
                if invoice.time_of_invoice.date() < date2:
                    yield invoice

    def get_replenishment_log(self, date1=None, date2=None):
        if date1 and date2:
            for log_entry in self.replenishment_log:
                if date1 < log_entry.time_of_invoice.date() < date2:
                    yield log_entry
        if date1 and not date2:
            for log_entry in self.invoices:
                if date1 < log_entry.time_of_invoice.date():
                    yield log_entry
        if date2 and not date1:
            for log_entry in self.invoices:
                if log_entry.time_of_invoice.date() < date2:
                    yield log_entry

    def add_invoice(self, journal, store, new_invoice):
        balance_before = store.balance(journal, item=new_invoice.item, balance_time=new_invoice.time_of_invoice)
        if new_invoice.quantity_sold <= balance_before:  # in case the function called by user
            if journal.invoices:
                post_quantity_sold_total = 0
                for invoice in journal.invoices:
                    if invoice.time_of_invoice > new_invoice.time_of_invoice and new_invoice.item == invoice.item.name:
                        post_quantity_sold_single_invoice = invoice.quantity_sold
                        post_quantity_sold_total += post_quantity_sold_single_invoice
                if post_quantity_sold_total > balance_before - new_invoice.quantity_sold:
                    Report.not_found(self, item=new_invoice.item)
                    return False, None
                else:
                    journal.invoices.append(new_invoice)
            else:
                journal.invoices.append(new_invoice)
            return new_invoice
        else:
            Report.not_found(self, item=new_invoice.item)
            return False, None

    def add_replenishment_log_entry(self, journal, new_log_entry):
        journal.replenishment_log.append(new_log_entry)
        return journal.replenishment_log


    def remove_invoice(self, invoice_id):
        for invoice in self.invoices:
            if invoice.id == invoice_id:
                self.invoices.remove(invoice)


class LogEntry:

        def __init__(self, time, item, quantity_added):
            self.records = {}
            self.time = time
            self.item = item
            self.quantity_added = quantity_added
            self.records.update({"Time": self.time, "Item": self.item, "Quantity_added": self.quantity_added, "Purchase price": item.purchase_price})


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

    def add_item_to_invoice(self, item, quantity, replenishment_journal):
        for entry in replenishment_journal.replenishment_log:
            if entry.item.name == item.name:
                self.records['Item'].append(item.name)
                self.records['Quantity'].append(quantity)
                self.records['Sell price'].append(item.sell_price)
                break
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

new_store.add_item(journal=new_journal, item_to_add=Milk, quantity_to_add=10)
new_store.add_item(journal=new_journal, item_to_add=Book, quantity_to_add=5)
# new_store.add_item(journal=new_journal, item_to_add=Mobile, quantity_to_add=10)

new_store.sell_item(journal_for_invoice=new_journal, item_to_sell=Book, quantity_to_sell=1)
# new_store.sell_item(journal_for_invoice=new_journal, item_to_sell=Mobile, quantity_to_sell=300)
new_store.sell_item(journal_for_invoice=new_journal, item_to_sell=Milk, quantity_to_sell=1)
new_store.sell_item(journal_for_invoice=new_journal, item_to_sell=Milk, quantity_to_sell=1)

new_list_of_invoices = new_journal.get_invoices(date1=datetime.date(2017, 1, 1), date2=datetime.date(2019, 1, 1))

new_invoice = Invoice(item=Book, quantity_sold=1,
                      time_of_invoice=datetime.datetime(year=2018, month=4, day=11, hour=12, minute=30, second=0, microsecond=0))
new_journal.add_invoice(journal=new_journal, new_invoice=new_invoice, store=new_store)

my_new_invoice = Invoice(item=Mobile, quantity_sold=23, time_of_invoice=datetime.datetime(year=2015, month=4, day=11, hour=12, minute=30, second=0, microsecond=0))
my_new_invoice.add_item_to_invoice(item=Book, quantity=123, replenishment_journal=new_journal)
new_report.print_invoice(my_new_invoice)
# new_report.print_invoice(invoices=new_list_of_invoices)