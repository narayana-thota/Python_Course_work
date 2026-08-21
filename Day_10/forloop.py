'''for loop is used when the number of iterations you know then we used the for loop 
for loop is used when you want to iterate in a sequence then we can use the for loop

syntax for loop is 
for i in (start,stop+1,size)


d={1:1,2:2,3:6,4:8,5:10}
for i in d.items():
    print(i)
    
s='narayana'
for i in s:
    print(i)
        
l=[92,67,80]
for i in l:
    print(i)
        
l=(92,67,80)
for i in l:
    print(i)
        
s={92,67,80}
for i in s:
    print(i)
    
d={1:1,2:2,3:6,4:8,5:10}
for i in d:
    print(i,d[i])

range() function is always give the numeric value sytax range(start,stop+1,step)


for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)
for i in range(5,0,-1):
    print(i)
    
for i in range(19,0,-2):
    print(i)
    
s='narayana thota'
for i in range(len(s)):
    print(i,s[i])

s='narayana thota'
for i in enumerate(s):
    print(i)
    
s='narayana thota'
for i,j in enumerate(s):
    print(i,j)
    
l=[1,2,3,4,5,6]
for i in range(len(l)):
    print(i,l[i])
    
t=(1,2,3,4,5,6)
for i in range(len(t)):
    print(i,t[i])
    
d={1:1,2:2,3:6,4:8,5:10}
print(d[1])

s='narayana thota'
for i in enumerate(s):
    print(i[0],i[1])
    
d={1:1,2:2,3:6,4:8,5:10}
for i in enumerate(d):
    print(i)
    
for i in range(1,11):
    if i==5:
        break
    print(i)
    
for i in range(1,11):
    if i==5:
        continue
    print(i)

d={6:1,2:2,3:6,4:8,5:10}
for i in enumerate(d):
    print(i)
    
for i in range(1,11):
    if i==5:
        break
    print(i)

#the else block is printed when there is no break statement is executed
for i in range(1,11):
    if i==15:
        break
    print(i)
else:
    print("End of the loop")
    
l=[1,2,3,4,5,6,7]
n=26
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"notfound")
    
pin=1234
for i in range(5):
    epin=int(input("enter name"))
    if epin==pin:
        print("unlock phone")
        break
    else:
        print("invalid pin")
else:
    print("try after 30 seconds")

n=14
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")
    '''
n=int(input("enter a number"))
lst=[]
for i in range(1,n):
    if n%i==0:
        lst.append(i)
print(f"factors of the {n}:{lst}")


    

