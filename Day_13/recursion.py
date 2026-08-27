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
'''
def display(s,n):
    if n==len(s):
        return 
    print(s[n])
    display(s,n+1)
display("narayana",0)


