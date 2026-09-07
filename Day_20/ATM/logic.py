data={
    123456:{'name':'narayana','pin':905937,'balance':60000,'history':[]},
    654321:{'name':'sameer','pin':565656,'balance':70000,'history':[]},
    654321:{'name':'sailesh','pin':420420,'balance':80000,'history':[]},
}

def login():
    global acc_num
    acc_num=int(input("Enter the account number"))
    pin=int(input("Enter the pin"))
    if acc_num in data and data[acc_num]['pin']==pin:
        print("Login successfully")
        return True
    else:
        print("Invalid Login")

def menu():
    print(f"Welcome to the ATM, {data[acc_num]['name']}")
    print('[c]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')

def checkbalance():
    print(f'Hello {data[acc_num]["name"]}')
    print('Current Balance:',data[acc_num]["balance"],end='\n\n')

def deposit():
    amount=int(input("Enter the Amount to Deposit"))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f"{amount} is deposited")
    print(f"{amount} is Deposited Successfully")
    checkbalance()

def withdraw():
    amount=int(input("Enter the Amount to Withdraw"))
    if data[acc_num]["balance"]>=amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]["history"].append(f'{amount} is withdraw')
        print(f"{amount} is withdraw Successfully")
        checkbalance()

def viewtransactions():
    if data[acc_num]["history"]:
        print("======== Transaction History ========")
        for i in data[acc_num]['history']:
            print(i)
    else:
        print("======= End of Transaction =======")











