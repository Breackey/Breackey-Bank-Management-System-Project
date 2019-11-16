#This is an ATM Simulator Python Project, works with console for now , I am working on designing a gui for it

#Step1: import modules from the python library that will provide functionality to the code
import pickle
import os  
import pathlib

#Step2: Create  a class for the bank accounts and define variables
class Account :
    accNo = 0    
    name = ''
    deposit=0
    type = ''
    
#define methods with class Account to give the class attributes
    def createAccount(self): #method for creating account
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [Current/Savings] : ")
        self.deposit = int(input("Deposit Initial amount(Minimum Ksh.500 for Savings and Ksh.1000 for current: "))
        print("\n\n\nAccount Created")

    def showAccount(self): #method for displaying accounts
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self): #method for modifying the accounts
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))
        
    def depositMoney(self,money): #method for depositing money in the account
        self.deposit += money
    
    def withdrawMoney(self,money):  #method for withdrawing money
        self.deposit -= money
    
    def report(self): #method for getting bank statement
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self): #method for dispgettinglaying account number
        return self.accNo
    def getAcccountHolderName(self): #method for getting Account Holder's Name
        return self.name
    def getAccountType(self):  #method for getting the account type
        return self.type
    def getDeposit(self):  #method for getting the deposit
        return self.deposit
    

def intro():  #text to be displayed when the system is launched
    print("\t\t\t\t**********************")
    print("\t\t\t\t WELCOME TO BREACKEY'S")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\r")
    print("\r")
    print("\t\t\t\tPress Enter Key To Proceed")
    print("\r")
    print("\r")  
    print("\r")      
    print("\t\t\t\t       Version 1.0")
    print("\t\t\t\t**********************")

    input()

def writeAccount():  #creates an account object
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():   #checks and displays an account details if it exists in the accounts.data file
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No records to display")
        
def displaySp(num):  #gets the account balance if the record exists in the accounts.data file
    file = pathlib.Path("accounts.data")
    
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def depositAndWithdraw(num1,num2): #method for depositing and withdrawing money from account
    file = pathlib.Path("accounts.data")
    if file.exists ():  #checks if record exists in the account.data file
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        os.remove('accounts.data')
        for item in mylist : #loops through the record
            if item.accNo == num1 :
                if num2 == 1 :
                    money = int(input("Enter the amount you wish to deposit : "))
                    item.deposit += money  #adds the money deposited to the money already in the account
                    print("Your account is updated")
                elif num2 == 2 :
                    money = int(input("Enter the amount you wish to withdraw : "))
                    if money <= item.deposit :  #checks if the money being withdrawn is less or equal to the money in the account
                        item.deposit -=money
                    else :
                        print("You cannot withdraw larger amount")
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")
    outfile = open('newaccounts.data','wb')  #writes accounts.data file in binary
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
def deleteAccount(num):  #deletes an account that exists in the accounts.data file
    file = pathlib.Path("accounts.data")
    if file.exists (): #checks whether the record exists in the accounts.data file
        infile = open('accounts.data','rb')  #opens accounts.data in binary
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):  #modifies account in the accounts.data file
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')  #renames newaccounts.data file to accounts.data file
    
# start of the program
opt=''
num=0
intro()

#displays the main menu as long as the option is not 8 which exits the system
while opt != 8:
    
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    opt = input()
    
    #appends option values to the Main menu 
    if opt == '1':
        writeAccount()
    elif opt =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif opt == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif opt == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif opt == '5':
        displayAll()
    elif opt == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif opt == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif opt == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    opt = input("Press Enter Key To Proceed : ")
    

