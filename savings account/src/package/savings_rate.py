from package.revenue import Revenue
from package.expenses import Expenses
class Rate(Revenue, Expenses):
    def __init__(self, time_period):
        self.total_rev = int(input("Total revenue: "))
        self.total_exp = int(input("Total expense: "))
        self.time_period = time_period
        self.time_type = input("Daily, Weekly or Monthly?: ")

    def savings_rate(self):
        savings = (self.total_rev - self.total_exp) / self.time_period
        return f'You earn ${savings} {self.time_type}'


