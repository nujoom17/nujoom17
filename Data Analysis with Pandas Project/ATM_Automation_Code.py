import pandas as pd

rf = pd.read_excel("C:/Users/HP/Documents/Bankpy.xlsx")


#function to ask user to continue or exit the session
def repeat_session():
    ext = input("Would you like to continue? (Y/N) ").upper()
    if ext in "Y":
        menu(0)
    else:
        print("Thank You for using AB Bank! Have a Nice day")

#function to let user withdraw money from the bank
def withdraw_money(b):
    bal = rf['Account Balance'].where(rf['Account No'] == b).values
    new_bal = [biw for biw in bal if pd.isnull(biw) == False]
    for biw in new_bal:
        new_balance_w=biw
    withdraw_amt=int(input(f"Enter the amount you want to withdraw? \n Maximum withdrawal limit {0.75*new_balance_w}"))
    if withdraw_amt > (0.75 * new_balance_w):
        print("Error! Enter smaller amount")
    else:
        filt = (rf['Account No'] == b)
        rf.loc[filt, 'Account Balance'] = new_balance_w - withdraw_amt
        rf.to_excel("C:/Users/HP/Documents/Bankpy.xlsx", index=False)

    repeat_session()

#function to let user deposit money into their bank
def deposit_money(b):
    bal = rf['Account Balance'].where(rf['Account No'] == b).values
    new_bal = [bi for bi in bal if pd.isnull(bi) == False]
    for bi in new_bal:
        new_balance_d=bi
    deposit_amt = int(input(f"Enter the amount you want to deposit? \n (**Maximum deposit limit: 10,000 ) \t :"))
    if deposit_amt > 10000:
        print("Error! Enter smaller amount")
        return deposit_money(b)
    else:
        filt=(rf['Account No']==b)
        rf.loc[filt,'Account Balance'] = new_balance_d + deposit_amt

        rf.to_excel("C:/Users/HP/Documents/Bankpy.xlsx", index=False)
    repeat_session()


#function to change service plan of user
def change_service_plan(b):
    service=rf['Service Plan'].where(rf['Account No']==b).values
    new_service=[ns for ns in service if pd.isnull(ns)==False]
    for ns in new_service:
        print(f"Your current service plan details: {ns}")
    e=input(f"Choose an option to update service plan for your account {b}\n" ""
            "1.Premium Savings\n"
            "2.General Savings\n"
            "3.Investment Account\n"
            "4.Affiliate Plan\n"
            "Enter an option (1-4)")
    if str(e)=="1":
        filt = (rf['Account No'] == b)
        rf.loc[filt, 'Service Plan'] = "Premium Savings"
    elif str(e)=="2":
        filt = (rf['Account No'] == b)
        rf.loc[filt,'Service PLan'] = "General Savings"
    elif str(e)=="3":
        filt = (rf['Account No'] == b)
        rf.loc[filt, 'Service PLan'] = "Investment Account"
    elif str(e)=="4":
        filt = (rf['Account No'] == b)
        rf.loc[filt, 'Service PLan'] = "Affiliate Plan"
    rf.to_excel("C:/Users/HP/Documents/Bankpy.xlsx", index=False)
    repeat_session()



#function to display account balance of user
def account_balance(b):
    bal=rf['Account Balance'].where(rf['Account No']==b).values
    new_bal=[bi for bi in bal if pd.isnull(bi)==False]
    for bi in new_bal:
        print(f"Account Balance for Account number {b}: {bi} ")
    repeat_session()

# function to let user input Account details and choose which account to operate on for this session
def choose_account(pin):
    b = int(input("Verify your Account Number: "))
    pin_d = rf['Pin code'].where(rf['Account No'] == b).values
    new_p = [p for p in pin_d if pd.isnull(p)==False]
    for p in new_p:
        print(p)

    if p == pin:
        a = rf['Name'].where(rf['Account No'] == b).values
        c = rf['Service Plan'].where(rf['Account No'] == b).values

        new_b = [y for y in c if pd.isnull(y) == False]
        new_a = [x for x in a if pd.isnull(x) == False]
        for x in new_a:
            for y in new_b:
                print(f"Hello {x}! Your Account Number is:{b} and your Service Plan is {y}")
                return menu(b)

    else:
        print("Error, Password does not match Account Number you entered")


def menu(b):
    print("Welcome to AB Bank, Please choose from one of the options below"

          "\n 1. View Account Balance"
          "\n 2. Withdraw Money"
          "\n 3. Deposit Money"
          "\n 4. Change Service Plan")
    user_i = int(input("\n Enter your selection(1-4)? \n"))
    if user_i not in range(1, 5):
        print("error, try again!")
        menu()
    else:
        if user_i == 1:
            account_balance(b)
        elif user_i == 2:
            withdraw_money(b)
        elif user_i == 3:
            deposit_money(b)
        elif user_i == 4:
            change_service_plan(b)

#function to initiate each session
def session():
    trials = 3
    while trials != 0:
        p = rf['Pin code'].values
        pin = int(input("Enter the Pin code: "))
        if not pin in p:
            trials -= 1
            print(f"Invalid Pin, Try again \n {trials} attempts remaining")
        else:
            return choose_account(pin)

#start of execution
session()

