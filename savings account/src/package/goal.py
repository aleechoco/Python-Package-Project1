from package.savings_rate import Rate
class Goal(Rate):
    def __init__(self, goal_amt):
        self.goal_amt = goal_amt
        self.savings = float(input("Savings rate(int): "))
        self.time_type = input("Days, Weeks or Months?: ")

    def point(self):
        arrange = round(self.goal_amt / self.savings)
        return f'You will get $ {self.goal_amt} in {arrange} {self.time_type}'