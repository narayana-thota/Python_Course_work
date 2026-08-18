"""follow=eval(input("enter you are following the account or not"))
if follow:
    close=eval(input("enter you are in clode friend list or not"))
    if close:
        print("store visible")
    else:
        print("you are not in close friend list")
else:
    print("first follow the account")
    
register=eval(input("enter you are registered or not"))
if register:
    fee=eval(input("tell you fee is paid or not"))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("pay fee")
else:
    print("first register")
    
link=eval(input("Tell whether the Link is active or not"))
if link:
    permission=eval(input("tell permission is granted or not"))
    if permission:
        print("File Opened Successfully")
    else:
        print("permission not granted")
else:
    print("link is not active")
    """
data={
    'karthik':{'status':True,'python':98,'mysql':94,'flask':99},
    'sailesh':{'status':False,'python':None,'mysql':None,'flask':None},
    'pavan':{'status':True,'python':20,'mysql':65,'flask':38},
    'narayana':{'status':True,'python':60,'mysql':65,'flask':68},
    'vijay':{'status':True,'python':80,'mysql':75,'flask':78},
    'sameer':{'status':True,'python':80,'mysql':85,'flask':88}
}
name=input("enter name")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"Hello{name}!!")
        print(f"your average score is {avg}")
        if avg>=90:
            print(f"Outstanding perfomance {name}")
        elif avg>=80:
            print(f"very good {name}")
        elif avg>=70:
            print(f"Good, work Hard {name}")
        elif avg>=35:
            print("Better Luck Next Time {name}")
        else:
            print("You Failed Exam {name}")
    else:
        print(f"{name} you didn't exam ")
print(f"{name} you are out of box ")