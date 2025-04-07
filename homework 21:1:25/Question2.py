class BankAccount():
    def __init__(self, account_number, balence):
        self.account_number = account_number
        self.balence = balence
    
    def deposit(self, amount):
        self.balence = self.balence + amount
    
    def withdraw(self, amount):
        if amount > self.balence:
            print("You don't have enough money!")
        else:
            self.balence = self.balence - amount

    def display_balence(self):
        print(f"Your current balence is {self.balence}")

hsbc = BankAccount(8172736, 300)

hsbc.display_balence()
hsbc.deposit(50)
hsbc.display_balence()
hsbc.withdraw(100)
hsbc.display_balence()
    