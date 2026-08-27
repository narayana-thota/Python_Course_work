
'''#local variable 
#a variable that we can accessed inside the function is called local variable
def lscope():
    n=10
    print("n value is :",n)
local()
print(n)

#global variable 
#a varible that can be accessed inside the fuction and outside the function is called is global variable
def gscope():
    print("n value is :" ,n)
n=10
print(n)
gscope()

#using global keyword we can access a local variable inside the function and outside the function also
def display():
    global n
    n=10
    print("Inside function:" ,n)
display()
print("outside the function:", 10)

->we have defone a local vaiable as global variable using global keyword then it overrides the global declares 
# outside the function also
->we can defined the local variable as a global variable we can not pass this variable as a 
parameter inside the function
def display():
    global n
    n+=10
    print("Inside function:" ,n)
n=10
display()
print("outside the function:", n)

#non local is give the access inside the file which gives the access inside the file it doesn't give access 
#outside the function

def display():
    name='thota'
    def update():
        nonlocal name
        name ='narayana'
        print("Inner name:",name )
    update()
    print("outer Function:", name)
display()
'''
#we can not use the built in function as variable if we use the  buitl in function as a variable then it losses it 
#functionality and act as a variable better to avoiod using the builtin function as variable
l=[1,2,3,4,5]
print(max(l))
print=20
print(max)


