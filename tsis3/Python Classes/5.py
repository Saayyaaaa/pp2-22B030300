class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def MyAccount (self):
        print("Account: ", self.owner)
        print("Initial balance: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Balance: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balance: ", (self.balance))

        else:
            self.balance -= amount
            print("Balance: ", self.balance)

my_account = Account("Saya", 1000)
my_account.MyAccount()
my_account.deposit(500)
my_account.withdraw(200)