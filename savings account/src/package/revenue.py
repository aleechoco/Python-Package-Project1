class Revenue:
    def __init__(self, amount):
        self.amount = amount
        self.rev = [self.amount]
    
    def add_revenue(self):
        add = int(input("Add cash revenue value here: $ "))
        self.rev.append(add)
        return self.rev

    def total_revenue(self):
        total = sum(self.rev)
        return f'The total revenue you have is {total}'

