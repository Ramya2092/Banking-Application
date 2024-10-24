class create_account:
    def get_name(self):
        self.name = input("Enter Your Name:\t")
        self.mobilenumber  = int(input ("Enter Your Mobile Number:\t"))
        self.email  = input ("Enter Your Email Address:\t")
        
    def get_accno(self):
        self.aadharno = int(input("Enter Your Last 4 digit of your AADHAR Number:\t"))
        if len(str(self.aadharno)) == 4:
            self.accno = self.aadharno
        else:
            self.aadharno1 = int(input("Please enter correct aadhar number:\t"))
            if len(str(self.aadharno1)) == 4:
                self.accno = self.aadharno1
            elif len(str(self.aadharno1)) != 4:
                self.aadharno2 = int(input("Please enter correcr aadhar number:\t"))
                if len(str(self.aadharno2)) == 4:
                    self.accno = self.aadharno2
                elif len(str(self.aadharno2)) != 4:
                    self.aadharno3 = int(input("Please enter correcr aadhar number:\t"))
                    if len(str(self.aadharno3)) == 4:
                            self.accno = self.aadharno3
                    else:
                        print("Your Aadhar is invalid.Please try after some times !!!")
                        exit()
        self.accno = int(str(self.accno)[::-1])

    def get_deposit(self):
        print("\nDeposit Amount for Savings Account(S) is minimum 500. \nDeposit Amount for Current Account(C) is minimum 1000.")
        self.accounttype = input("\nChoose Your Account Type: C / S \n")
        self.deposite = int(input("Enter the deposit amount : "))
        if (((self.accounttype == 'C') or (self.accounttype == 'c' )) and self.deposite >= 1000):
            print("\n       =====================================")
            print("\n       YOUR ACCOUNT WAS SUCCESSFULLY CREATED")
            print("\n       =====================================")
        elif (((self.accounttype == 'S') or (self.accounttype == 's' )) and self.deposite >= 500):
            print("\n      =====================================")
            print("\n      YOUR ACCOUNT WAS SUCCESSFULLY CREATED")
            print("\n      =====================================")
        else:
            print("\nYour are choosing wrong account type OR wrong deposit amount entered. \nSo, you cannot create the account. \nPlease enter the proper details. \n\nThank you !!!")
        self.balance = self.deposite
        
    def show_account(self):
        print("\nYour Account Details")
        print("======================")
        print("Account Holder Name: ",self.name.upper())
        
        print("Account Number     : ",self.accno)
        if self.accounttype == "C" or self.accounttype == "c":
            self.accounttype = "Current Account"
        elif self.accounttype == "S" or self.accounttype == "s":
            self.accounttype = "Savings Account"
        else:
            pass
        print("Account Type       : ",self.accounttype)
        print("Balance            : ",self.balance)
        print("Email              : ",self.email)
        print("Ph Number          : ",self.mobilenumber)
    
    def modify_account(self):
        acc_num = int(input("Enter Your Account Number:\t"))
        if acc_num == self.accno:
            print("\n1. Change Email Id\n2. Change Mobile Number\n3. Change your Email ID & Mobile Number")
            self.num = int(input("\nPlease Enter Your Option:\t"))
            if self.num == 1:
                self.email = input("\nPlease Enter Your Email Address:\t")
                print("\n*****YOUR DETAILS ARE UPDATED SUCCESSFULLY***")
            elif self.num == 2:
                self.mobilenumber  = int(input ("\nPlease Enter Your Mobile Number:\t"))
                print("\n*****YOUR DETAILS ARE UPDATED SUCCESSFULLY***")
            elif self.num == 3:
                self.email = input("\nPlease Enter Your Email Address:\t")
                self.mobilenumber  = int(input ("Enter Your Mobile Number:\t"))
                print("\n*****YOUR DETAILS ARE UPDATED SUCCESSFULLY***")
        else:
            print("\nPlease Enter Correct Account Number")

    def deposite_amount(self):
        amount = int(input("Enter Your Deposite Amount:\t"))
        self.balance = self.balance + amount
        print("\nDeposited Successfully")
        print("Your Balance Is : ",self.balance)

    def withrawal_amount(self):
        amount = int(input("Enter Your Withrawal Amount:\t"))
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("\nWithDrawal Successfully")
            print("Your Balance Is : ",self.balance)
        else:
            print("Insufficient Balance")
            

    def balance_enquiry(self):
        acc_num = int(input("Enter Your Account Number:\t"))        
        if acc_num == self.accno:
            print("Your Balance Is : ",self.balance)







      










