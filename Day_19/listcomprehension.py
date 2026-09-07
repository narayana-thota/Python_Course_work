l=[1,2,3,4,5]
lst=[i for i in l if i%2==0 ]
print(lst)

l=[i for i in range(5)]
print(l)

l=[i for i in range(0,10,2)]
print(l)

n=16
f=[i for i in range(1,n+1) if n%i==0]
print(f)

l=[1,2,3,4,5]
lst=[i if i%2==0 else "odd" for i in l ]
print(lst)