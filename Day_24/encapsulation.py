'''
#creating the public private protected attributes
# class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):
        return self.__password
    @property
    def access(self):
        return self._post
obj=Instagram("narayana",123456789)
print(obj.username)
print(obj.getpassword())
print(obj.access)'''

#modifying the public private and protected attributes
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
    @property
    def access(self):
        return self._post
    @access.setter
    def access(self,newpost):
        self._post.append(newpost)
obj=Instagram("narayana",123456789)
print(obj.username)
print(obj.getpassword())
print(obj.access)
obj.username="narayanathota"
obj.setpassword(926780)
obj.access="intro"
obj.access="strings"
print(obj.username)
print(obj.getpassword())
print(obj.access)



    





