# Custom exception is created by inheriting the Exception Class which is built-in, which raises
# when a person tries to withdraw amount greater than account balance
class InSufficientFundsException(Exception):
    pass


# This exception raises when a user tries to withdraw negative or zero Amount
class InValidAmountException(Exception):
    pass


class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def __int__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise InValidAmountException("In valid Amount!! Amount Should be greater than zero")
        self.__balance += amount
        print(f"Successfully deposited.. The Account Balance is {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InValidAmountException("In valid Amount!! Amount Should be greater than zero")
        if amount > self.__balance:
            raise InSufficientFundsException("Your Account Balance is Low...")
        self.__balance -= amount
        print(f"Successfully withdrawn. The Current Balance is : {self.__balance}")

    def check_balance(self):
        return f"Your Account balance is : {self.__balance}"

    def simulation(self):
        print("Hi There...Welcome to ATM")
        while True:
            print("Select an option : ")
            print("1 : Deposit\n2 : Withdraw\n3 : Check Balance\n4 : Exit")
            choice = int(input("Enter your choice (1-4) : "))

            if choice == 1:
                try:
                    money = int(input("Enter amount to deposit : "))
                    atm.deposit(money)
                except ValueError:
                    print("Invalid Input!! Please Enter Integers greater than zero")

            elif choice == 2:
                try:
                    money = int(input("Enter amount to withdraw : "))
                    atm.withdraw(money)
                except ValueError:
                    print("Invalid Input!! Please Enter Integers greater than zero")
                except InSufficientFundsException as e:
                    print(str(e))

            elif choice == 3:
                print(self.check_balance())

            elif choice == 4:
                print("Thank You!!!")
                break
            else:
                print("Invalid Choice. Please choose among 1-4")
balance = 25768
atm = ATM(balance)
atm.simulation()
