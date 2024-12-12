print("Welcome to ABC bank")
class Bank:
    balance = 50000
    withdrawal = 0  
    def viewOptions(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("0. Exit")
    def deposit(self):
        amt = int(input("Enter amount to be added: "))
        if amt < 100:
            print("Amount should be greater than 100")
        elif amt % 100 != 0:
            print("The amount should be in multiples of 100")
        elif amt > 50000:
            print("The amount to be deposited should be less than 50K")
        else:
            self.balance += amt
            print("Amount deposited successfully")
    def withdraw(self):
        if self.withdrawal >= 3:
            print("Transaction limit reached")
            return
        amt = int(input("Enter amount to be withdraw"))
        if self.balance > 500:
            if amt < 100:
                print("Amount to be withdraw must be greater than 100")
            elif amt % 100 != 0:
                print("The amount should be in multiples of 100")
            elif amt > self.balance:
                print("Insufficient balance")
            elif amt > 20000:
                print("Amount should not be greater than 20K")
            else:
                self.balance -= amt
                self.withdrawal += 1
                print("Balance withdrawn successfully")
        else:
            print("Insufficient balance")
    def display(self):
        print("Current balance is:", self.balance)
    def validate(self):
        for i in range(3, 0, -1):
            pin = int(input("Enter PIN number"))
            if pin == 1234:
                self.withdrawal = 0  
                self.viewOptions()
                for _ in range(7):
                    n = int(input("Choose an option"))
                    match n:
                        case 1:
                            self.deposit()
                        case 2:
                            self.withdraw()
                        case 3:
                            self.display()
                        case 0:
                            print("Exit")
                            exit(0)
                        case _:
                            print("Enter valid option")
                break
            else:
                if i == 1:
                    print("Card blocked")
                else:
                    print(f"Invalid PIN number. Chances left: {i - 1}")
obj = Bank()
obj.validate()
