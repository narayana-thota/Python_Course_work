''''#lambda function anonymous function it doesn't require any name to create
syntax of the lambda function is 
var=lambda arg:exp
->it takes no of argumtents and it executes only one expression

#printing greeting
wish=lambda name:f"my name is {name}"
print("narayana")

#calculating the Gst
gst=lambda price:price+price*0.18
print(gst(500))

#calculating the Average
avg=lambda a,b,c:(a+b+c)//3
print(avg(1,2,3))

#checking the given number is even or odd
iseven=lambda n: "even" if n%2==0 else "odd"
print(iseven(10))

#checking the large number
largest=lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(1,2,3))

#square of the given number
square=lambda n: n**2
print(square(2))

#to check the given character is vowel or not 
s=lambda c: "Vowel" if c in 'aeiouAEIOU' else "consanant"
print(s('n'))


#lambda function using in list

l=[1,2,3,4,5,6,7]
update=list(map(lambda i:i+10,l))
print(update)

#lambda function using in tuple
t=(789,421,3453,56565,565656)
discount=list(map(lambda i:i-180.3,t))
print(discount)

t=(789,421,3453,56565,565656)
discount=list(filter(lambda i:i>1000,t))
print(discount)


#extracting the domain names
l=["narayana@google.com","narayana@gmail.com","narayana@mechease.com"]
lst=list(map(lambda i:i.split('@')[-1],l))
print(lst)


#sum of the list using the reduce function
from functools import reduce 
l=[656,5656,656,565,262,565]
res=reduce(lambda sum,i:sum+i,l)
print(res)

#product of the list using the reduce function
from functools import reduce 
l=[656,5656,656,565,262,565]
res=reduce(lambda p,i:p*i,l)
print(res)


#using lambda checking the availability
seats={'s1':True,
      's2':False,
      's3':True,
      's4':False,
      's5':True}
a=list(filter(lambda i:seats[i]!=True,seats))
print(a)


#printing the products greater than 50
products={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}
res=list(filter(lambda i:products[i]>50,products))
print(res)


#sorting using the values
products={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))


'''

