'''data={}
lst=[]
n=int(input("enter n"))
for _ in range(n):
    i,j=input().split()
    data[i]=j
for i in data:
    print(i.ljust(20),data[i])
for j in data.values():
    lst.append(int(j))
print(f"total sum of the products is:{sum(lst)}")

data={
    'sugar':120,
    'rice':70,
    'oil':120,
    'eggs':60,
    'butter':70
}
for i in data:
    print(i.ljust(20),data[i])
prod=input("enter the products").split()
bill=0
for i in prod:
    print(i.ljust(20),data[i])
    bill+=data[i]
print("Total bill".ljust(20),bill)


s='python programming'
data={}
for i in s:
    if i in data:
        data[i]+=1
    else:
        data[i]=1
print(data)

s='aaaaaabbbbbbbccccccaa'
l={}
for i in s:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
print(*tuple(l.items()))

s='ppppppyyyyytt'
print(len(s))
c=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))

if 10==10:
    pass
for i in range(1,10):
    pass
class verify:
    pass
    
email='sdfgh'
password='1234'
assert email!='' and password!='','userneeds to give and pwd'
'''
def apply_discount(price, discount):
    # Sanity check: Price must be 0 or higher
    assert price >= 0, "Error: Price cannot be a negative number!"
    
    # Sanity check: Discount must be a valid percentage
    assert 0 <= discount <= 100, "Error: Discount must be between 0 and 100!"
    
    return price - (price * (discount / 100))

# This works perfectly. (The asserts are True, so they are ignored)
print(apply_discount(100, 20))  

# This crashes instantly with an AssertionError and prints your custom message
print(apply_discount(-50, 20))






