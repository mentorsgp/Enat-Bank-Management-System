class BankAccount:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            print(f"${amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def show_transactions(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print("-", transaction)


def main():
    print("=== Welcome to Python Banking System ===")

    owner = input("Enter account holder name: ")
    account = BankAccount(owner)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print("Thank you for using the Banking System.")
            break

        else:
            print("Invalid choice. Try again.")


if name == "main":
    main()