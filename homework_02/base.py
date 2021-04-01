from abc import ABC
from exceptions import LowFuelError,NotEnoughFuel

class Vehicle(ABC):
    weight = None
    started = None
    fuel = 0.0
    fuel_consumption = 0.0

    def __init__(self,weight,fuel,fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __getattr__(self,sample):
            print(f"getattr method has been called, param={sample}")
        #return super().__getattr__(sample)
    def start(self):
        if self.started == 1:
            print('we are already flying')

        if not self.started:
            if self.fuel >  0:
                self.started = 1
                print('стартууем!')
            else:
                raise LowFuelError('Zero fuel')
            
            
    def move(self,distance:int):
        if self.fuel < self.fuel_consumption * distance:
            raise NotEnoughFuel()
        print('distance confirmation')


v0 = Vehicle(10,10500,2)
v0.start()
v0.start()
v0.move(10)
