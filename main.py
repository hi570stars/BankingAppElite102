print("Welcome to BetterBanking\nA bank that gives back.")
##check balance, deposit, withdraw, create account, delete account, modify account
first = input("1. Log in\n2. Create an account")
if first == 1:
    userName = input("Enter username: ")
    #check if userName is a valid username in the username column
    #if it is not prompt to create an account (make first = 2)
    #if it is, then go on to:
        password = input("Enter password: ")
        #check if password matches user name
if first == 2:
    userName = input("Enter username")
    #add this userName and corresponding password to the database w/ 0$. 
    #ask them to also create a PIN duh!
second = input("What would you like to do with us today?\n1. Check Your Balance\n2. Withdraw money\n3. Deposit Money\n4. Delete Account\n5. Edit Account\n6. Exit and Log Out")
if second == 1:
    check_balance()
elif second == 2:
    withdraw_money()
elif second == 3:
    deposit_money()
elif second == 4:
    delete_account()
elif second == 5:
    edit_account()
elif second ==6:
    exit_log_out()

def check_balance():
    #return the value in the "UserBalance" column of mySQL

def withdraw_money():
    money_to_be_withdrawn = input ("How much money do you want withdrawn (type number only - no commas, no $, etc.)?")
    if money_to_be_withdrawn > 0 && money_to_be_withdrawn < check_balance():
        yes_no = input (f"Are you sure you want to withdraw ${money_to_be_withdrawn}?")
        if yes_no == "yes":
            #return the value in the "UserBalance" column of mySQL - the amount the user wants withdrawn
            #change the value in "UserBalance" to userbalance - m_t_b_w
        else:
            #userbalance stays the same.

def deposit_money():
    money_to_be_deposited = input ("How much money do you want deposited (type number only - no commas, no $, etc.)?")
    if money_to_be_deposited > 0 && money_to_be_deposited < 10000:
        yes_no = input (f"Are you sure you want to deposit ${money_to_be_deposited}?")
        if yes_no == "yes":
            #return the value in the "UserBalance" column of mySQL + the amount the user wants deposited
            #change the value in "UserBalance" to userbalance + m_t_b_d
        else:
            #userbalance stays the same.

def delete_account():
    yes_no = input (f"Are you sure you want to delete {##getusername##}'s account?")
    if yes_no == "yes":
        #delete that whole user's column
    
def edit_account():
    edit_what = input("What would you like to edit? 1. Username 2. Password 3. PIN")
    if edit_what == 1:
        edit_user = input("What would you like your username to be? ")
        yes_no = input (f"Are you sure you want to edit your username to {edit_user}?")
        if yes_no == "yes":
            #change username to edit_user
    elif edit_what == 2:
        edit_pass = input("What would you like your password to be? ")
        yes_no = input (f"Are you sure you want to edit your password to {edit_pass}?")
        if yes_no == "yes":
            #change password to edit_pass
    elif edit_what == 3:
        edit_PIN = input("What would you like your PIN to be? ")
        #check if pin is 4 digits (4 + NUMS ONLY)!
        yes_no = input (f"Are you sure you want to edit your PIN to {edit_PIN}?")
        if yes_no == "yes":
            #change password to edit_PIN

def exit_log_out():
    yes_no = input("Log out? ")
    if yes_no == "yes":
        #go back to database?

