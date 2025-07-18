import json
accounts ={}
def load_accounts():
    global accounts
    try:
        with open("accounts.json","r") as file:
            data= file.read()
    except FileNotFoundError as e:
        print(f"Uups, file: {accounts} not found")
        print(f"Exception: {e} was raised")
        accounts = {}

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)
def create_accounts():
    name= input("enter ur name: ")
    if name in accounts:
        print("ur acc is exisit")
    else:
        balance = float(input("enter balance: "))
        accounts[name] = balance
        save_accounts()
        print("acc create")
def deposit():
    name = input("enter acc name:")
    if name in accounts:
        amount= float(input("enter deposit amount: "))
        accounts[name] += amount
        save_accounts()
        print("deposit success ")
    else:
        print("acc not found ")

def withdraw():
    name = input("enter acc name: ")
    if name in accounts:
        amount = float(input("enter withdrawal : "))
        if amount > accounts[name]:
            print("not true")
        else:
            accounts[name] =accounts[name]- amount
            save_accounts()
            print("withdrawal success ")
    else:
        print("acc not found ")

def check_balance():
    name = input("enter acc name: ")
    if name in accounts:
        print("ur balance is: ", accounts[name])
    else:
        print("acc not found.")

load_accounts()
while True:
    print("1_create acc")
    print("2_deposit")
    print("3_withdraw")
    print("4_check Balance")
    print("5_exit")
    choice = input("choose: ")
    if choice == '1':
        create_accounts()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("see ya")
        break
    else:
        print("Error")