class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        #return f"User: {self.name}, Balance: ${self.account_balance}"
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self,other_user,amount):
        if self.account_balance - amount < 0:
            print("Not enough funds")
            return self
        self.account_balance -= amount
        other_user.account_balance += amount
        #return f"User: {self.name}, Balance: ${self.account_balance}\nUser: {other_user.name}, Balance: ${other_user.account_balance}"
        return self


guido=User("Guido van Rossum", "guido@python.com")
monty=User("Monty Python", "monty@python.com")

# print(guido.name)
# print(monty.name)

# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)

# print(guido.account_balance)
# print(monty.account_balance)

michael=User("Michael Jordan", "michael@python.com")
john=User("John Rosales", "john@python.com")
mark=User("Mark Guillen", "mark@python.com")


# michael.make_deposit(100)
# michael.make_deposit(30)
# michael.make_deposit(180)
# michael.make_withdrawal(20)
# michael.display_user_balance()

michael.make_deposit(100).make_deposit(30).make_deposit(180).make_withdrawal(20).display_user_balance()

# john.make_deposit(500)
# john.make_deposit(40)
# john.make_withdrawal(25)
# john.make_withdrawal(10)
# john.display_user_balance()

john.make_deposit(500).make_deposit(40).make_withdrawal(25).make_withdrawal(10).display_user_balance()

# mark.make_deposit(1000)
# mark.make_withdrawal(15)
# mark.make_withdrawal(100)
# mark.make_withdrawal(85)
# mark.display_user_balance()

mark.make_deposit(1000).make_withdrawal(15).make_withdrawal(100).make_withdrawal(85).display_user_balance()

michael.transfer_money(mark,500)
michael.display_user_balance()
mark.display_user_balance()

michael.transfer_money(mark,50)
michael.display_user_balance()
mark.display_user_balance()
