class car:
    def __init__ (self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def driving(self):
        print("car is used for driving")
    
class Audi(car):
    def __init__ (self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower
    def driving(self):
        print("it is a self driving car")

audiq7=Audi(4,5,"diesel",200)

print(audiq7.horsepower)
print(audiq7.windows)
audiq7.driving()
audiq7.selfdriving()

car1 = car(4,5,"diesel")
print(car1)
print(audiq7)

print(dir(audiq7))
print(dir(car1))