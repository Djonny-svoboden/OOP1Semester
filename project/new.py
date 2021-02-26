class Printer:
    inkCounter=200
    def __init__(self,name,paperCount,droch,maxPapepCount):
        self._name=name
        self.paperCount=paperCount
        self.droch = droch
        self.maxPapepCount=maxPapepCount
        print(self._name, ":now exist", Printer.inkCounter, "now ink in printer",self.paperCount,"now paper")

    def print(self):
        Printer.inkCounter=Printer.inkCounter-(self.droch*10)
        if self.droch<=self.paperCount:
            self.paperCount=self.paperCount-self.droch
        print("printed ",self.droch,"lists","inkcounter is ",Printer.inkCounter)
    def cleaning(self):
        Printer.inkCounter=Printer.inkCounter-50
        print('printer now clean')
    def paperFilling(self):
        if self.paperCount<self.maxPapepCount:
            self.paperCount=self.maxPapepCount
            print("paper now is ",self.paperCount)
    def getName(self):
        return self._name
    @staticmethod
    def is_on(state):
        if (state=="on"):
            print("device is on")
        elif(state=="off"):
            print("device is off")
        else:
            ("bruj")

pr1=Printer("Kanon",7,3,11)
# pr1.is_on("on")
print(pr1.getName())
print("paper is",pr1.paperCount)
pr1.paperFilling()
