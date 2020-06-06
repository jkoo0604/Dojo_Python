class User:
	def __init__(self,username,email_address, accountid=1, int_rate=0.02, balance=0):
		self.name = username
		self.email = email_address
		self.account = BankAccount(accountid, int_rate, balance)
		
		#How to tell one account from another within BankAccount class?

	def __repr__(self):
		return f"*******************************\nName: {self.name}\nEmail: {self.email}\nAccount Type: {self.account.accountid}\nBalance: {self.account.account_balance}\nYield: {self.account.int_rate}"

	def make_deposit(self,amount):
		self.account.deposit(amount)
		return self

	def make_withdrawal(self,amount):
		self.account.withdraw(amount)
		return self

	def display_user_balance(self):
		print(f"User: {self.name}, Balance: ${self.account.account_balance}")
		return self

	def transfer_money(self,other_user,amount):
		self.account.transfer(other_user,amount)
		return self


class BankAccount:
	def __init__(self, accountid=1, int_rate=0.02, balance=0): #Create multiple checking or savings for same user? Unique identifier?
		self.accountid = accountid
		self.int_rate = int_rate
		self.account_balance = balance
		

	def deposit(self, amount):
		self.account_balance += amount
		return self
		
	def withdraw(self,amount):
		if self.account_balance - amount < 0:
			print("Insufficient funds: Charging a $5 overdraft fee")
			self.account_balance -= (amount + 5)
		else:
			self.account_balance -= amount
		return self
		
	def display_account_info(self):
		print(f"Account: {self.accountid}, Balance: ${self.account_balance}")
		return self
		
	def yield_interest(self):
		self.account_balance *= (1+self.int_rate)
		return self

	def transfer(self,other_user,amount):
		if self.account_balance - amount < 0:
			print("Insufficient funds")
			return False
		else:
			self.account_balance -= amount
			other_user.account.account_balance += amount
			print("Transfer successful")
			return True

#Add new user
User1=User("Jane Doe","jane@python.com")
User2=User("Monty Python","monty@python.com", 2, 0.025, 1000)

User1.make_deposit(1000).make_deposit(500).make_withdrawal(150).transfer_money(User2,3000)
User1.make_deposit(1000).make_deposit(500).make_withdrawal(150).transfer_money(User2,30)
print(User1)
print(User2)


#how to access different accounts for each user? (update all other methods - deposit, withdraw, transfer)