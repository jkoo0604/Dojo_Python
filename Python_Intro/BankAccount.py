class BankAccount:
	def __init__(self, accountid, int_rate=0.01, balance=0): # don't forget to add some default values for these parameters!
		self.accountid = accountid
		self.int_rate = int_rate
		self.account_balance = balance
        

	def deposit(self, amount):
		self.account_balance += amount
		return self
		
	def withdraw(self,amount):
		if self.account_balance - amount < 0:
			print("Insufficient funds: Charging a $5 fee")
			self.account_balance -= (amount + 5)
		else:
			self.account_balance -= amount
		return self
		
	def display_account_info(self):
		print(f"Account: {self.accountid}, Balance: ${self.account_balance}")
		return self
		
	def yield_interest(self):
		self.account_balance = (1+self.int_rate) * self.account_balance
		return self


Acct1=BankAccount(1, 0.015)
Acct2=BankAccount(2,0.01,300)

Acct1.deposit(200).deposit(1000).deposit(150).withdraw(100).yield_interest().display_account_info()
Acct2.deposit(2000).deposit(500).withdraw(100).withdraw(80).withdraw(120).withdraw(50).yield_interest().display_account_info()

