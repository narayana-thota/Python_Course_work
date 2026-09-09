'''
#Single Inheritence
class Whatsappv1:
    def message(self):
        print("you can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("upload the status")
v1=Whatsappv1()
v1.message()
v2=Whatsappv2()
v2.message()
v2.status()

class Whatsappv1:
    def message(self,message):
        self.message=message
        print(f"{self.message}")
class Whatsappv2(Whatsappv1):
    def status(self,message,upload):
        self.message=message
        self.upload=upload
        print(f"{self.message},{self.status}")
      
v1=Whatsappv1()
v1.message("hi")
v2=Whatsappv2()
v2.status("hi","single")

#Multilevel Inheritence
class Whatsappv1:
    def message(self):
        print("you can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("upload the status")
class Whatsappv1:
    def message(self):
        print("you can send a message")
class Whatsappv3(Whatsappv2):
    def group(self):
        print("you can create group")
v1=Whatsappv1()
v1.message()
v2=Whatsappv2()
v2.message()
v2.status()
v3=Whatsappv3()
v3.message()
v3.status()
v3.group()


#multilevel Inheritence
class Whatsappv1:
    def message(self):
        print("you can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("upload the status")
class Whatsappv3:
    def groups(self):
        print("you can create group")
class Whatsappv4:
    def community(self):
        print("you can create the community now in these version")
class Whatsappv5(Whatsappv4,Whatsappv3,Whatsappv2):
    def channels(self):
        print("in these version we create the chaneels")
    

v5=Whatsappv5()
v5.message()
v5.status()
v5.groups()
v5.community()
v5.channels()
'''
class Whatsappv1:
    def message(self):
        print("you can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("upload the status")
class Whatsappv3(Whatsappv1):
    def groups(self):
        print("you can create group")
class Whatsappv4(Whatsappv1):
    def community(self):
        print("you can create the community now in these version")
v1=Whatsappv1()
v1.message()
v2=Whatsappv2()
v2.message()
v2.status()
v3=Whatsappv3()
v3.message()
v3.groups()
v4=Whatsappv4()
v4.message()
v1=Whatsappv1()
v4.community()




