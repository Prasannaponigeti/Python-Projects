import logging as lg
lg.basicConfig(
    filename = "app-log",
    level = lg.DEBUG,
    format = "[%(asctime)s- %(levelname)-s]-%(message)s"
)

#Total operations
operations=(
    "1. Balance\n"
    "2. Withdraw\n"
    "3. Deposit\n"
    "4. Transfer\n"
    "5. History\n"
    "6.Exit\n"
)

#Account table
account_table={
    12345:6789,
    54321:9876
}
#Users Table
users_table= {12345:['PPrasanna','prasanna123@gmail.com', 10000],54321:['PMallika', 'mallika123@gmail.com',50000]}

#Checking Valid user
def valid_user(user_name:int,password:int):
    lg.debug("User in login page")
    if user_name in account_table:
        if account_table[user_name]== password:
            lg.info("User successfully loggined")
            print("User successfully loggined")
            return True
        else:
            lg.warning("Please check your login credentials")
            print("Please check your login credentials")
            return False
    else:
        lg.warning("Please check your login credentials")
        print("Please check your login credentials")
        return False
    
#Checking User Balance Function
def balance(user_name:int):
    lg.debug("User in Balance page")
    if user_name in users_table:
        amount= users_table[user_name][2]
        lg.info(f"{user_name} user current balance is{amount}")
        print(f"{user_name} user current balance is{amount}")
    else:
        lg.warning("User not found")
        print("user not found")

#Withdraw Amount function
def withdraw(user_name):
    lg.debug("User in Withdraw page")
    amount = users_table[user_name][2]
    withdraw_amount=int(input("Please enter withdraw amount:"))
    if amount >= withdraw_amount:
        users_table[user_name][2]-=withdraw_amount
        lg.info(f"{withdraw_amount} withdraw successful and current balance is{users_table[user_name][2]}")
        print(f"{withdraw_amount} withdraw successful and current balance is{users_table[user_name][2]}")

#Deposit Amount function
def deposit(user_name):
    lg.info("User in deposit page")
    deposit_amount=int(input("Please enter amount:"))
    if user_name in users_table:
        users_table[user_name][2]+=deposit_amount
        lg.info(f"{deposit_amount} deposit successful and current balance is{users_table[user_name][2]}")
        print(f"{deposit_amount} deposit successful and current balance is{users_table[user_name][2]}")


#Transfer Amount function
def transfer(user_name):
    lg.debug("User in transfer page")
    receiver_account = int(input("Enter Receiver account number:"))
    amount= int(input("enter amount:"))
    lg.info(f"receiver account is{receiver_account} and amount is {amount}")
    current_amount= users_table[user_name][2]
    if receiver_account in users_table:
        if current_amount>= amount:
            #amount updation in users table
            users_table[user_name][2]-=amount
            users_table[receiver_account][2]+=amount
            lg.info(f"{amount} transfer successful and current balance is{users_table[user_name][2]}")
            print(f"{amount} transfer successful and current balance is{users_table[user_name][2]}")
        else:
            lg.warning("Insufficient amount")
            print("Insufficient amount")
    else:
        lg.warning(f"{receiver_account} not found")
        print(f"{receiver_account} not found")



#Check History function
def history(user_name):
    lg.info("User in history page")
    print("History function under development process.....")
    pass

#exit function
def exit_fun():
    lg.info("User in exit page")
    print("Successfully Existed, Thank you!")
    return True


# Choose_operation function defination
def choose_operation(account_no, choice):
    lg.info(f"Selected Operation is {operations[choice-1]}")
    val=False
    if choice==1:
        balance(user_name=account_no)
    elif choice==2:
        withdraw(user_name=account_no)
    elif choice==3:
        deposit(user_name=account_no)
    elif choice==4:
        transfer(user_name=account_no)
    elif choice==4:
        transfer(user_name=account_no)
    elif choice==5:
        history(user_name=account_no)
    elif choice==6:
        val = exit_fun()
    else:
        print("Enter choice between(1-6)")
    if val:
        return val
    

if __name__ == "__main__":
    print("Welcome to the Online codegnan Banking")
    lg.info("Welcome to the Online codegnan Banking")
    user_name = int(input("Please, Enter account number: "))
    password =int(input("Please Enter pin number: "))
    lg.info(f"User credentials are {user_name} and {password}")
    while True:
        if valid_user(user_name, password):
            print(*operations)
            lg.info(operations)
            choice = int(input("Please select operation (1-6): "))
            exit_fun_val = choose_operation(account_no = user_name, choice = choice)
            if exit_fun_val:
                break
        else:
            lg.warning("User not found,please check with your login credentials")
            print("User not found,please check with your login credentials")
            
        

    