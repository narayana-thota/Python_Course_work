'''
#positive number or negative number
n=int(input("enter a number"))
if n>0:
    print("positive number")
else:
    print("negative number")
    
#even or odd
n=int(input("enter a number"))
if n%2==0:
    print("even number")
else:
    print("odd number")
    
#check the number divisible by 5 or not
n=int(input("enter a number"))
if n%5==0:
    print("Divisible by 5")
else:
    print("not divisible by 5")
    
#check for leap year
n=int(input("enter a number"))
if n%4==0:
    print("leap year")
else:
    print("not leap year")
    
#check the given number is divisible 3 and 7
n=int(input("enter a number"))
if n%3==0 and n%7==0:
    print("Divisible by 3 and 7")
else:
    print("not divisible by 3 and 7")
    
#checking the given student is pass or fail
marks=int(input("enter marks"))
if marks>=35:
    print("pass")
else:
    print("fail")
    
#check if they number is 3 digit number or not
n=str(input("enter a number"))
if len(n)>=3:
    print("3 digit number")
else:
    print("not a 3 digit number")
    
#check if character is vowel
lst=['a','e','i','o','u']
s=input("enter string")
if s in lst:
    print('vowel')
else:
    print('not vowel')
    
#check the greatest of two numbers
a=int(input("enter a "))
b=int(input("enter b"))
if a>b:
    print(f'{a} is greater ')
else:
    print(f'{b} is greater')

#check the smallest of two numbers
a=int(input("enter a "))
b=int(input("enter b"))
if a<b:
    print(f'{a} is smaller ')
else:
    print(f'{b} is smaller')
    
#check if the number is zero or not
a=int(input("enter"))
if a==0:
    print("the given number is 0")
else:
    print("the given number is not zero")
    
#check the given number is muultiple of 10 or not
n=int(input("enter n"))
if n%10==0:
    print(f'the given number is multiple of 10')
else:
    print(f'the given number is not multiple of 10')
#eligible for vote or not
age=int(input("enter n"))
if age>18:
    print(f'eligible for vote')
else:
    print(f'not eligible for vote')
#to check the given number in range or not
ra=int(input("enter the range"))
n=int(input("enter a number"))
for i in range(1,ra):
    if 1<=n<=i:
        print("the given number in range")
        break
#Check if number is square of another
n=int(input("enter a number"))
for i in range(n):
    if n==i*i:
        print(f'{n} is square of {i}')
#check the strings are equal 
a=str(input("enter a"))
b=str(input("enter b"))
if sorted(a)==sorted(b):
    print('strings are equal')
#check if the given number is prime or not
n=int(input("enter a number"))
for i in range(2,n):
    if n%i!=0:
        print("prime number")
        break
        '''
s=input("enter character")
if s.isupper():
    print("upper case letter")

    
   




