







class Bank:
    penalty_amount = 5

    def __init__(self, int_rate, balance):
        self.interestRate = int_rate
        self.balance = balance
        self.penalty = 0
        # print(f"Hello!!! Welcome to the Magic Money machine")
        # return self
# deposit(self, amount) - increases the account balance by the given amount
    
    def deposit(self, amount):
        # amount = float(input(f"Enter amount to be deposited: "))
        # if Bank.deposit(self, amount):
        self.balance += amount 
        print("Amount Deposited", amount)
        return self
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
#  if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.balance - amount <0:
            self.balance -= (amount + Bank.penalty_amount)
            self.penalty += Bank.penalty_amount
            print("Insufficienct Funds Charging a $5 Fee")
        else:
            self.balance -= amount
            print("Amount withdrawn", amount)
            return self
# display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        # self.display_account_info()
        # print(f" Balance: {amount}")
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if (self.balance >0):
                self.balance += self.balance * self.interestRate
                print("Interest Earned:", self.interestRate * self.balance)
                return self

checking = Bank(.02, 10)

user2 = Bank(.05, 3000)
checking.deposit(23).deposit(50).deposit(678).deposit(455).withdraw(45).yield_interest().display_account_info()
# user1.deposit (400)

# to the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)

user2.deposit(200).deposit(300).withdraw(20).withdraw(30).withdraw(40).withdraw(50).yield_interest().display_account_info()


class User:
    def __init__(self, name, int_rate, balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        self.account = Bank(.02,200)
        

    def make_deposit(self, amount):
        self.account.deposit (200)
        print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(43)
        print(self.account.balance)
        return self

    def display_user_balance(self, amount):
        self.account.balance -= amount
        print(f" New Balance: {self.account.balance}")
        return self



pam = User("pam", "pam@aol.com", 34)
# pam.make_deposit(50).display_user_balance().make_withdrawal(43)
pam.make_deposit(30)
pam.make_withdrawal(40)
pam.display_user_balance(amount)