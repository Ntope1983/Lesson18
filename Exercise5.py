from datetime import date


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)


class Credit(Payment):
    def __init__(self, amount, number, exp_date):
        super().__init__(amount)
        self.number = number
        self.exp_date = exp_date

    def __str__(self):
        return super().__str__() + f"--Credit id:{self.number}--Exp_Date: {self.exp_date}"


class Check(Payment):
    def __init__(self, amount, number, bank_code):
        super().__init__(amount)
        self.number = number
        self.bank_code = bank_code

    def __str__(self):
        return super().__str__() + f"--Check Number:{self.number}--Bank_Code: {self.bank_code}"


class Order:
    def __init__(self, date_order, payment):
        self.date_order = date_order
        self.payment = payment

    def __str__(self):
        return f" Date: {self.date_order} Amount:{self.payment}"


class Customer:
    def __init__(self, name, address, orders=None):
        self.name = name
        self.address = address
        if orders is None:
            self.orders = []
        else:
            self.orders = orders

    def __str__(self):
        orders_result = "--".join([str(order) for order in self.orders])
        result = f"Costumer:{self.name}--Address:{self.address}--Orders:{orders_result}"
        return result

    def place_order(self, order):
        self.orders.append(order)


def main():
    c = Customer("Jim Psoun", "Papadaki 78")
    c.place_order(Order("20201020", Payment(12.12)))
    c.place_order(Order("20201021", Credit(22.12, "12937-2139883-388", "20231203")))
    c.place_order(Order("20201022", Check(32.12, "12389-123898-239", "3834720-98/3")))
    print(c)
main()
