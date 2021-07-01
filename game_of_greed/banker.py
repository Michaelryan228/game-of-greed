class Banker:

  def __init__(self, balance=0, shelved=0):
    self.balance = balance
    self.shelved = shelved

  def shelf(self, points = 0):
    self.shelved += points

  def bank(self):
    amount_deposited = self.shelved
    self.balance += self.shelved
    self.shelved = 0
    return amount_deposited

  def clear_shelf(self):
    self.shelved = 0
    
