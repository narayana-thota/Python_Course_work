'''a function call it self again and again is called recursion until it reached the base condition
syntax
def fun(arguments):
    base condition:
        return 
    fun(update function)
fun(parameters)

def display(n):
    if n==11:
        return 
    print(n)
    display(n+1)
display(1)

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)

def display(n):
    if n==n[-1]:
        return
    print(n[n])
    display(n+1)
display("narayana")

def display(n):
    l=0
    if l==len(n)-1:
        return
    print(n[l])
    display(l+1)
n=str(input())
display(n)

def display(s,n):
    if n==len(s):
        return 
    print(s[n])
    display(s,n+1)
display("narayana",0)

def display(n):
    if n==11:
        return 
    print(11-n)
    display(n+1)
display(1)

#if we print outside the function recursion then it will return in the reverse order
def display(n):
    if n==11:
        return 
    display(n+1)
    print(n)
display(1)
#reversing string
def display(s,n):
    if n==len(s):
        return
    display(s,n+1)
    print(s[n],end=' ')
display("codeganan",0)
    
def display(s,ind,w):
    if len(s)-w+1==ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
s=input("enter the string")
w=int(input("enter width"))
display("narayana thota",0,w)


#Sum of the lst
def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=[10,20,30,40,50]
print(display(l,0))

#printing the sum of the number
def display(l):
    if l==0:
        return 0
    return l%10 + display(1//10)
l=43567
print(display(l))

#factorail of a given number
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter a number"))
print(fact(n))


#fibonacci series
n=int(input("enter the number"))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=' ')
        
#fibonacci series using recursion

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(20):
    print(fib(i))
    

def solve():
    input_data = int(input())
    if not input_data:
        return
    n = int(input_data)
    row = 1
    while row <= n:
        for col in range(row):
            if row % 2 != 0:
                print("*", end=" ")
            else:
                print(row, end=" ")
        print()
        row += 1
'''
def solve():
    input_data = input()
    if not input_data:
        return
    n = int(input())
    row = 1
    while row <= n:
        for col in range(row):
            if row % 2 != 0:
                print("*", end=" ")
            else:
                print(row, end=" ")
        print()
        row += 1
solve()


        

    