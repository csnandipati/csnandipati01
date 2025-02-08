balance=1000
def deposit(amount):
    global balance
    balance+=amount
    print(f"deposited:rupees(amount)")

def Withdraw(amount):
    global balance
    if balance>=amount:
       balance-=amount
       print(f"Withdraw:rupeers(amaount)")
    else:
        print("insufficient balance")

def balance_enquiry():
    print(f"Your Balance: Rupees(balance)")

while True:
    print("\n=====ATM Menu======")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Balance Enquiry")
    print("4.Exit")

    choice = int(input("Enter your Choice:"))

    if choice == 1:
        amount=int(input("Enter amount to deposit:"))
        deposit(amount)
    elif choice ==2:
        amount = int(input("Enter amount to withdraw:"))
        Withdraw(amount)
    elif choice ==3:
        balance_enquiry()
    elif choice == 4:

        print("thankyou for using the Atm")
        break
else:
    print("invalid choice.please try again.")
