import json
import os

USER_DATA_FILE = "atm-users.json"  # File to store user data

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:   # "r" open in read mode
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
                else:
                    return {}
            except json.JSONDecodeError:
                return {}
    return {}
    
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:  # "w" open in write mode
        json.dump(users, file, indent=4)  # To make it more readable by formatting it with 4 spaces per identation level
        
class User:    # User class
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}$")
            print(f"Deposit successful! New Balance: {self.balance}$")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}$")
            print(f"Withdrawal successful! New Balance: {self.balance}$")
        else:
            print(f"Insufficient balance or invalid amount!")
            
    def check_balance(self):
        print(f"Current Balance: {self.balance}$")
        
    def view_transactions(self):
        print("Transaction History: ")
        for transaction in self.transactions:
            print(transaction)
    
class ATM:
    def __init__(self):
        self.users = load_users()
        
    def create_account(self):
        name = input("Enter your name: ")
        pin = input("Set a 4 digit PIN: ")
        if name in self.users:
            print("Account already exists!")
            return
        self.users[name] = {"pin": pin, "balance": 0, "transactions": []}
        save_users(self.users)
        print("Account created successfully!")
        
    def login(self):
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        if name in self.users and self.users[name]["pin"] == pin:
            print(f"Welcome, {name}!")
            return User(name, pin, self.users[name]["balance"])
        print("Invalid credentials!")
        return None
    
    def update_user(self, user):
        self.users[user.name]["balance"] = user.balance
        self.users[user.name]["transaction"] = user.transactions
        save_users(self.users)
        
def main():  # Main Function
    atm = ATM()
    
    while True:
        print("\nWelcome to Smart ATM ")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            atm.create_account()
        elif choice == "2":
            user = atm.login()
            if user:
                while True:
                    print("\nATM Menu")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. View Transactions")
                    print("5. Logout")
                    action = input("Choose an option: ")
                    
                    if action == "1":
                        user.check_balance()
                    elif action == "2":
                        amount = float(input("Enter amount to deposit: "))
                        user.deposit(amount)
                    elif action == "3":
                        amount = float(input("Enter amount to whithdraw: "))
                        user.withdraw(amount)
                    elif action == "4":
                        user.view_transactions()
                    elif action == "5":
                        atm.update_user(user)
                        print(" Logged out successfully!")
                        break
                    else:
                        print("Invalid Choice!")
        
        elif choice == "3":
            print("Thank you for using Smart ATM!")
            break
        else:
            print("Invalid choice! Try again.")
            
if __name__ == "__main__":
    main()        