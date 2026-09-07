class Flipkart:
    discount=30

    @classmethod
    def updateddiscount(cls):
        cls.discount=40
        print("updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name=name
        self.phoneno=phoneno
        self.address=address
        print("welcome to flipkat",self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount} is going on....")

obj=Flipkart()

obj.info("narayana",9059374985,"perakalapudi")
obj.updateddiscount()
obj.banner()

obj.info("sameer",1234567890,"vijayawada")
obj.updateddiscount()
obj.banner()

obj.info("sailesh",9874563210,"vijayawada")
obj.updateddiscount()
obj.banner()

