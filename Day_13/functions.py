'''def gst(price):
    print("origina price:",price)
    print("final price:",price+price*0.18)
gst(50)
gst(100)
gst(150)
gst(200)

def table(t,n):
    for i in range(1,n+1):
        print(f'{t}*{i}={t*i}')
n=int(input("enter n"))
t=int(input("enter t"))
table(t,n)

#multiplication table
def table(n):
    print(f'{n}-Table')
    print('---------------')
    for i in range(1,11):
        print(f'{n}*{i}={n*i}')
for i in range(1,21):
    table(i)
    
#is leap year or not
def leap(year):
    if year%400==0 or(year%4==0 and year%100!=0):
        return "leap year"
    else:
        return "not leap year"
print(leap(2026))
print(leap(2025))
print(leap(2024))
print(leap(2023))
print(leap(2022))
print(leap(2021))

#check the given number is prime number or not
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
n=int(input("enter n"))
prime(n)

#positional arguments
def display(name,age,gender):
    print(name)
    print(age)
    print(gender)
display("sammer",21,"m")

#keyword arguments
def display(name,age,gender):
    print(name,end=' ')
    print(age,end=' ')
    print(gender)
display(age=21,gender='male',name="narayana")

#default arguments
"""
in default arguments these arguments should be at last after the positional arguments

def display(age,gender,name='narayana'):
    print(name)
    print(age)
    print(gender)
display("narayana thota",21,"m")
'''
#variable length arguments
def display(**names):
    print(names)
display(n1='thota')
display(n1='thota',n2='narayana')


    