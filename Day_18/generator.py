'''def reels():
    data=['1.100','2.200','3.300','4.400,','5.500']
    for i in data:
        yield i
res=reels()
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

def number(n,i):
    if i!=n:
        yield i
    print(i)
    number(n,i+1)
res=number(5,0)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
'''
def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
res=countdown()
for i in res:
    print(i)

def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
res=factors(16)
for i in res:
    print(i)

def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
            else:
                yield i
res=prime(100)
for i in res:
    print(i,end='')






