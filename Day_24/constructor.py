'''class Instagram:
    def __init__(self,name,password):
        self.name=name
        self.password=password
        print(f"welcome {self.name}")
name=input("enter name")
age=int(input("enter age"))
obj=Instagram(name,age)
'''
class Instagram:
    def __init__(self):
        pass
    def show(self,name,age):
        self.name=name
        self.age=age
        print(f"welcome {self.name}")
name=input("enter name")
age=int(input("enter age"))
obj=Instagram()
obj.show(name,age)
