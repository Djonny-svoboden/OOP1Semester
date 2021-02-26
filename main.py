class Animal:
    kind = "warm-blooded"
    __counter=0

    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        Animal.__counter+=1
        print(self.name,":now",Animal.__counter,"animals exist")
    def __del__(self):
        Animal.__counter-=1
        print("Now",Animal.__counter,"animals left")
    def sayHello(self):
        print("hello",self.name,"mySpeed =",self.speed)
    def speedUp(self,delta):
        self.speed=self.speed+delta
    def speedDown(self,delta):
        if(self.speed>=delta):
            self.speed=self.speed-delta
    def stop(self):
        self.speed=0
    def getCounter(self):
        return self.__counter
an1=Animal("Kitty",5)
# an2=Animal("Puppy",2)
# an3=Animal("Tiger",4)
# an3.sayHello()
# an3.speedUp(20)
# an3.speedDown(15)
# an2.sayHello()
# an2.stop()
print(an1.name)
print(an1.getCounter())
del an1
# del an2
# del an3

