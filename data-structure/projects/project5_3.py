from project5_2 import Queue
from datetime import datetime
from time import sleep


class SuperMarket(Queue):
    def __init__(self):
        super().__init__()
        self.total_customer = 0
        self.total_time = []
        self.customers_detail = {}

    def working_time(self):
        if not 8 <= datetime.now().hour < 14:
            return False
        return True

    def is_open(self):
        if not self.working_time():
            return "super market is closed"
        return "super market is open"

    def add_customer(self, customer_name):
        if not self.working_time():
            return "super market is closed"
        customer_data = {"name": customer_name, "arrival_time": datetime.now()}
        self.enqueue(customer_data)
        self.customers_detail[customer_name] = customer_data
        self.total_customer += 1
        return f"{customer_name} entered the supermarket"

    def cash_register(self):
        if self.is_empty():
            return "there are no customers in super market"
        customer = self.dequeue()
        customer = customer.data
        checkout_time = datetime.now()
        customer["check-out time"] = checkout_time
        shopping_time = (
            customer["check-out time"] - customer["arrival_time"]
        ).total_seconds() / 60
        customer["shopping time"] = shopping_time
        self.total_time.append(shopping_time)
        return f"The customer {customer['name']} after passing {shopping_time} his purchase was completed."

    def average_waiting_time_per_person(self):
        if not self.total_time:
            return 0.0
        return sum(self.total_time) / len(self.total_time)

    def statistics(self):
        return f"""supermarket report
        status : {self.is_open()}
total customers : {self.total_customer}
served customer : {len(self.total_time)}
customer in queue : {len(self)}
average shopping time : {self.average_waiting_time_per_person()}"""


market = SuperMarket()
print(market.add_customer("Alice"))
print(market.add_customer("Bob"))
print(market.add_customer("Charlie"))
print(market.cash_register())
sleep(3)
print(market.cash_register())
sleep(7)
print(market.cash_register())
print(market.statistics())
