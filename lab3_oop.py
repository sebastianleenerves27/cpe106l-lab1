class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

owner_name = input("Enter account name: ")
try:
    initial_balance = float(input("Enter initial balance: "))
except ValueError:
    initial_balance = 0

account = BankAccount(owner_name, initial_balance)
print(f"\nAccount created for {account.owner} with balance {account.balance}\n")

#Deposit
try:
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
except ValueError:
    print("Invalid input, skipping deposit.")

#Withdraw
try:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
except ValueError:
    print("Invalid input, skipping withdrawal.")

#FinalBalance
print(f"\nFinal balance for {account.owner}: {account.balance}")

