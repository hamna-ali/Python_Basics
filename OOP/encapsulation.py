class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Hamna Ali", 10000)
account.deposit(2000)
print(f"Balance of {account.owner} is:", account.get_balance())
