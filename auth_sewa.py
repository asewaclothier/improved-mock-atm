from random import randint
from datetime import datetime #import date from date time library

now = datetime.now()
timeframe = now.strftime("%B %d, %Y. %H:%M:%S") #format of date month day, year. TIME - hour:minute:second
database = {
    4082576389 : ["Emmanuel", "Oladele", "adesewa@zuri.com", "bloodyhell", 0] #data base for users
}

def init():
    
    print(f"Welcome to the Omoologo's bank \n{timeframe}")
    
    haveAccount = int(input("Do you have an account with us? Press (Y) Yes or (N) NO :\n"))
       
    # if statement confirm if user is in data base, and if not registering user
    if haveAccount == "Y":
        login()
    elif haveAccount == "N":
        print(register())
    else:
        print("Invalid option selected")
        init()

#func. for logining 
def login():

    print("Kindly Login to your account")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
    
    login()

#create a function to register new user into data base
def register():
    print ("***** Fill in the details below to register. *****")

    email = input("What is your email address?\n")
    first_name =  input("What is your first name?\n")
    last_name =  input("What is your last name?\n")
    password = input("Create a password for yourself?\n")
    balance = 0

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password, balance]

    print("Your account has been created")
    print(f"-- ---- ----- ------ \nYour account number is: {accountNumber} \nMake sure to keep it safe \n-- ---- ----- ------"  )

    login()

#different operations registered user can performed 
def bankOperation(user):

    print(f"Welcome {user[0]} {user[1]}")
 
    selectedOption = int(input("What would you like to do? 1. Deposit 2. Withdrawal 3. Logout 4. Complaints 5. Check account balance 6. Exit \n"))

    if (selectedOption == 1):
        depositOperation(user)
    elif (selectedOption == 2):
        withdrawalOperation(user)
    elif (selectedOption == 3):
        logOut()
    elif (selectedOption == 4):
        complaintsOperation(user)
    elif (selectedOption == 5):
        checkBalance(user)   
    elif (selectedOption == 6):
        exit()
    else:
        print("Invalid option selected, TRY AGAIN.")
        bankOperation(user)

#creatE a withdrawal function
def  withdrawalOperation(user):
    print(f"Current Balance as at  {timeframe} is: {user[-1]} naira")
    amount_to_withdraw = int(input("How much would you like to withdrawl? \n"))
    if amount_to_withdraw > user[-1]:
        deposit = int(input("You have insufficient funds. Would you like to make a deposit or withdraw a lesser amount? Press (Y) Yes or (N) NO, I would withdraw a lesser amount. \n"))
        if deposit == "Y":
            depositOperation(user)
            another_operation(user)
        elif deposit == "N":
            withdraw_different_amount = int(input("Would you like to withdraw a different amount or log out? Press (Y) Yes or (N) NO \n"))
            if withdraw_different_amount == "Y":
                withdrawalOperation(user)
            else: 
                logOut()
    else:
        user[-1] -= amount_to_withdraw
        print(f"Take Cash. \nNew account balance is:{user[-1]}" )
        another_operation(user)

#creating a deposit function
def depositOperation(user):
    amount_deposited = int(input("How much would you like to  deposit? \n"))
    user[-1] += amount_deposited
    print(f"New account balance as at {timeframe} is: {user[-1]} naira"))
    another_operation(user)

#creating a complaints function
def complaintsOperation(user):
    input("Kindly input your complaints here.\n")
    print("Thanks for the feedback %s %s, we would get back to you in the next 24 hours. Till then STAY JIGGY." %(user[0], user[1]))
    another_operation(user)

#creating a function to check balance
def checkBalance(user):
    print(f"Your balance as at {timeframe} is: {user[-1]} naira"))
    another_operation(user)

#creatinig a log out func.
def logOut():
    print("********* Logging Out... *********")
    print("********* LOGGED OUT *********")
    exit()
    login()

#creating a loop function
def another_operation(user):
    option = int(input("Would you like to perform another operation? (1) Yes or (2) No\n"))
    if option == 1:
        bankOperation(user)
    elif option == 2:
        logOut()
    else:
        print("Invalid option, read carefully before selecting.")
        another_operation(user)


#function to generate specific account numbers for registered users in a data base
def generateAccountNumber():
    print("Generating Account Number")
    Start = 1,000,000,000
    End = 9,999,999,999
    return randint(Start, End)

init()
