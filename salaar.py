class BankAccount:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited.")
        else:
            print("Invalid amount.")
            
    def withdraw(self, amount):
        if amount <= 0:
            print("invalid amount.")
            
        elif amount > self.balance:
            print("Insufficient balance.")
            
        else:
            self. balance -= amount
            print("Amount withdrawn.")
            
    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
        
        
name = input("Enter your name:")

account = BankAccount(name)

while True:
    
    print("/n---BANKING SYSTM ---")
    print("1. Deposit")
    print("2. withdraw")
    print("3. check Balance")
    print("4. Exit")
    
    choice = input("Enter choice:")
    
    if choice =="1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)
        
    elif choice =="2":
        amount = float(input("Enter amount"))
        account.withdraw(amount)
        
    elif choice == "3":
        account.show_balance()
        
    elif choice == "4":
        break   
                                                     
    
    