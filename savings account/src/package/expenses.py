class Expenses:
    def __init__(self, amount):
        self.amount = amount
        self.exp = [self.amount]
    
    def add_expenses(self):
        add = int(input("Add cash expense value here: $ "))
        self.exp.append(add)
        return self.exp

    def total_expenses(self):
        total = sum(self.exp)
        return f'The total expense you have is {total}'
