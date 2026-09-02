'''#pass by value if we pass a value it doesn't effect inside the function
#pass by reference if we we pass a value by reference it effects inside the function also
#int
def display(n):
    n+=10
    print("Inside",n)
n=10
display(n)
print("outsie", n)

#float
def display(n):
    n+=10.3
    print("Inside",n)
n=10.3
display(n)
print("outsie", n)

#complex
def display(n):
    n+=10+3j
    print("Inside",n)
n=10+3j
display(n)
print("outsie", n)

#STRING
def display(n):
    n+='narayana'
    print("Inside",n)
n='thota'
display(n)
print("outsie", n)

#list
def display(n):
    n.append(6)
    print("Inside",n)
n=[1,2,3,4,5]
display(n)
print("outsie", n)

#tuple
def display(n):
    n+=(6,7)
    print("Inside",n)
n=(1,2,3,4,5)
display(n)
print("outsie", n)

#SET
def display(n):
    n.add(7)
    print("Inside",n)
n={1,2,3,4,5}
display(n)
print("outsie", n)

#Dict
def display(n):
    n[6]=7
    print("Inside",n)
n={1:2,3:4,5:6}
display(n)
print("outsie", n)
'''







