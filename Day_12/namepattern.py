''''
#D
n=int(input("enter n"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#B
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
 #E   
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#F  
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#c
n=int(input("enter n"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#G
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#H
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==m or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#I
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or (j<=m and j==m) or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#z
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Y  
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#K
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i==j and i>=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
#M
n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or  (i==j and i<=m)  or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input("enter n"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m)  or :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
