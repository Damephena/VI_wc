""" 
---------------------------------------------------------------------------------
Build a command-line Banking Application with the following functionalities:
Application starts with a prompt to the user with the following options:
Press 1: create account
Press 2: transaction
2. Create account: This should prompt you to enter an email/or unique identity, and then a password. You must check your data structure to make sure the account is unique before creating the new account
3. Transaction: Authenticate the user by prompting for a password, if the password is correct, user is authenticated and show the following options:
Press 1: check balance
Press 2: deposit
Press 3: withdraw
Press 4: transfer
if the password is incorrect, tell the user that they are not authorized and go back to the create account option
4. check balance: query your data structure to check the balance of the authenticated user
5. deposit: prompt the user to enter an amount, then add the amount to the users balance
6. withdraw: prompt the user to enter an amount, if the user does not have money in their account, tell them to deposit and move to the deposit prompt. If they user has money, print out the amount withdrawn and the available balance,
7. transfer: prompt the user to enter an email of the person they want to transfer to, prompt for the amount, deduct the amount from the authenticated users balance, add the amount to the beneficiaries account,
Ensure that you clog all the gaps for those process flows that i have not explicitly defined

""" 

# sample data
bank_accounts = {
    'okoye@gmail.com' : {'password': '12345678', 'balance': 100},
    'ada@gmail.com' : {'password': '12345678', 'balance': 450}
}

def verify_account(email):
    if email in bank_accounts.keys():
        return email
    return False

def validate_password(password, confirm_password):
    if len(password) >=6:
        if password == confirm_password:
            return password
    else:
        return False


def create_account():
    print("\n+++++ CREATE NEW ACCOUNT +++++\n")
    new_email = str(input("Enter a valid email: ")).lower()

    #check email format has @ and '.'
    if len(new_email) > 5 and ('@' in new_email) and ('.' in new_email):
        
        if verify_account(new_email):
            print("Email Already exists! Try again")
            create_account()
        else:
            new_password = str(input("Enter a valid password: "))
            confirm_password = str(input("Confirm password: "))

            if validate_password(new_password, confirm_password):
                bank_accounts[new_email] = {'password' : new_password, 'balance': 0.00}
                print("Your account has been created successfully!")
                home_page()
            else:
                print("======= Password too short or Password Mismatch ======\n Should be atleast 6 characters. Confirm new password")
                create_account()
    else:
        print("Invalid Email address")
        create_account()


def authenticate_user():
    print("\n>>>>>>>>> LOG IN >>>>>>>>\n")
    user_email = str(input("Enter email: ")).lower()
    user_password = str(input("Enter password: "))

    if user_email in bank_accounts.keys():
        if bank_accounts[user_email]['password'] == user_password:
            transaction_options(user_email)
    else:
        print("You are not authorized!\n ==============================\n Create an account\n" )
        create_account()


def transaction_options(account):
    print("\n******* TRANSACTION PAGE *********\n")
    more_options = int(input(" Press 1: check balance\n Press 2: deposit\n Press 3: withdraw\n Press 4: transfer\n Press 0: HOME\n"))
    if more_options == 1:
        check_balance(account)
    elif more_options == 2:
        make_deposit(account)
    elif more_options == 3:
        make_withdrawal(account)
    elif more_options == 4:
        make_transfer(account)
    elif more_options == 0:
        home_page()
    else:
        print("Enter a valid action")
    transaction_options(account)


def check_balance(account):
    print("\n====================== CHECK BALANCE ===================\n")
    print("Your account balance is: ", bank_accounts[account]['balance'])
    transaction_options(account)


def make_deposit(account):
    print("\n====================== MAKE DEPOSIT ===================\n")
    deposit_amount = int(input("Input amount to be deposited:\n"))
    bank_accounts[account]['balance'] = bank_accounts[account]['balance'] + deposit_amount
    new_balance = bank_accounts[account]['balance']

    print("Amount deposited: ", deposit_amount, "\nAvailable balance: ", new_balance)
    transaction_options(account)


def make_withdrawal(account):
    print("\n====================== MAKE WITHDRAWAL ===================\n")
    amount = int(input("Input amount to withdraw:\n "))
    
    if bank_accounts[account]['balance'] == 0.00:
        print("You have no money in your account. Kindly make deposit and try again.\n")
        make_deposit(account)
    elif bank_accounts[account]['balance'] < amount:
        print("Cannot withdraw more than you have in your account\n ")
        make_deposit(account)
    else:
        bank_accounts[account]['balance'] = bank_accounts[account]['balance'] - amount
        current_balance = bank_accounts[account]['balance']
        print("\n============== Withdrawal Successful ==========\n Amount withdrawn: ", amount, "\nCurrent available balance: ", current_balance)
    transaction_options(account)


def make_transfer(account):
    print("\n====================== MAKE TRANSFER ===================\n")
    transfer_amount = int(input("Enter amount to be transfered: "))
    beneficiary = str(input("Enter beneficiary's email: ")).lower()

    if transfer_amount > bank_accounts[account]['balance']:
        print("You have *** insuffient *** funds to perform transaction! Kindly make deposit and try again\n")
        transaction_options(account)
    else:
        # confirm beneficiary's email in DB structure
        if verify_account(beneficiary):
            bank_accounts[beneficiary]['balance'] = bank_accounts[beneficiary]['balance'] + transfer_amount

            # User's current balance after making a transfer
            bank_accounts[account]['balance'] = bank_accounts[account]['balance'] - transfer_amount
            account_balance = bank_accounts[account]['balance']
            print("------- Transfer Successful -------\nAmount transfered: ", transfer_amount, "\nBeneficiary's email: ", beneficiary, "\nAccount Balance: ", account_balance)
            transaction_options(account)
        else:
            print("\n------- Invalid Beneficiary -----\n Kindly verify email address")
            transaction_options(account)


def home_page():
    print("\n>>>>>>>>>>>>> HOME PAGE <<<<<<<<<<<<<<<<<")
    landing_page = int(input("Hello,\n Press 1: create account\n Press 2: transaction\n Press 0: Quit program\n"))
    
    if landing_page == 1:
        create_account()

    elif landing_page == 2:
        authenticate_user()

    elif landing_page == 0:
        quit()
    else:
        print("Enter a valid option")
        home_page()

home_page()