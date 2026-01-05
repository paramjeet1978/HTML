class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")
    def withdrawAmount(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        if self.balance - amount < 1000:
            raise Exception("Cannot withdraw. Minimum balance of 1000 must be maintained.")
        self.balance -= amount
        print(f"Withdrew: ${amount}. New balance: ${self.balance}")
    def display(self):
        print(f"Current balance: ${self.balance}")
    
atm = ATM(1000)
while True:
    try:
        print("Select action:\n1. Deposit\n2. Withdraw\n3. display\n3. Exit")
        action = int(input("Enter action : "))
        if action == 1:
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif action == 2:
            amount = float(input("Enter amount to withdraw: "))
            atm.withdrawAmount(amount)
        elif action == 3:
              atm.display()
        elif action == 4:
             print("Exiting ATM. Goodbye!")
             break
        else:
             print("Invalid action. Please enter deposit, withdraw, or exit.")
    except Exception as e:
        print(f"Error: {e}")