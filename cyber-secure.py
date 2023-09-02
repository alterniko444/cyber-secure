class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age  = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age  ", self.age)
        print("Gender ", self.gender)


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : $", self.balance)
    
    def view_balance(self):
        self.show_details()
        print("Account balance: $", self.balance)
        
print("=== Welcome to the Bank ===")
accounts={}
ch=int(input("Enter 1 to proceed or 0 to exit:"))
while (ch==1):
        print("\nMenu:")
        print("1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            new_user = Bank(name, age, gender)
            accounts[name] = new_user
            print("Account created successfully!")

        elif choice == 2:
            name = input("Enter your name: ")
            if name in accounts:
                user = accounts[name]
                while name:
                    print("\nAccount Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. View Balance")
                    print("4. Go Back")
                    account_choice = int(input("Enter your choice: "))

                    if account_choice == 1:
                        amount = float(input("Enter amount to deposit: "))
                        user.deposit(amount)
                    elif account_choice == 2:
                        amount = float(input("Enter amount to withdraw: "))
                        user.withdraw(amount)
                    elif account_choice == 3:
                        user.view_balance()
                    elif account_choice == 4:
                        break
                    else:
                        print("Invalid choice! Please select a valid option.")
            else:
                print("Account not found!")

        elif choice == 3:
            print("Thank you for using the Bank!")
            break

        else:
            print("Invalid choice! Please select a valid option.")
if (ch==0):
    print("Thank you for using the Bank!")
elif (ch!=0 and ch!=1):
    print("Invalid choice")











