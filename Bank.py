class BankAccount:
  interest_rate = 0.01
  accounts = []

  def __init__(self):
    balance = 0
    self.balance = balance
    __class__.accounts.append(self)


  def deposit(self, number):
    self.balance += number

  def withdraw(self, number):
    if number <= self.balance:
      self.balance -= number


  @classmethod
  def total_funds(cls):
    total = 0
    for acct in cls.accounts:
      total += acct.balance
    return total
      

    
  @classmethod
  def add_interest(cls):
    for acct in cls.accounts:
      interest = acct.balance * cls.interest_rate
      acct.balance += interest
    
 



def main():
  my_account = BankAccount()
  your_account = BankAccount()
  print(my_account.balance) #--> 0
  print(BankAccount.total_funds()) #--> 0
  my_account.deposit(200)
  your_account.deposit(1000)
  print(my_account.balance) #--> 200
  print(your_account.balance) #--> 1000
  print(BankAccount.total_funds()) #--> 1200
  BankAccount.add_interest()
  print(my_account.balance) #--> 202.0
  print(your_account.balance) #--> 1010.0
  print(BankAccount.total_funds()) #--> 1212.0
  my_account.withdraw(50)
  print(my_account.balance) #--> 152.0
  print(BankAccount.total_funds()) #--> 1162.0

main()
