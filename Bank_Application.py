from BankModule import *
a = create_account()
while True:
    print("\n *** BANKING SYSTEM ***  \n")
    print("1. Create New Account")
    print("2. Display Account Details")
    print("3. Modify Your Account")
    print("4. Deposite Amount")
    print("5. Withdrawal Amount")
    print("6. Balance Enquiry")
    print("7. Exit")

    data = int(input("\nPlease Enter Your Option: "))
    if data == 1:
        a.get_name()
        a.get_accno()
        a.get_deposit()
    elif data == 2:
        a.show_account()
    elif data == 3:
        a.modify_account()
    elif data ==4:
        a.deposite_amount()
    elif data == 5:
        a.withrawal_amount()
    elif data == 6:
        a.balance_enquiry()
    elif data == 7:
        exit()
    else:
        print("Invalid Option Enter")