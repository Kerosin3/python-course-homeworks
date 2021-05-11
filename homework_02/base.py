from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, ValueSettingError


class Vehicle(ABC):

    def __init__(self, weight=None, fuel=0.0, fuel_consumption=0.0):
        self.started = False #default
        try:
            fuel = float(fuel)
            fuel_consumption = float(fuel_consumption)
        except ValueError:
            raise ValueSettingError
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __getattr__(self, sample): #accessing unknown
        print(f"getattr method has been called, param={sample}")

    def start(self):
        if self.started:
            return
        if self.fuel <= 0:
            raise LowFuelError
        self.started = True

    def move(self, distance: int):
        if self.fuel < self.fuel_consumption * distance:
            raise NotEnoughFuel
        self.fuel -= (self.fuel_consumption * distance)  # substract fuel being consumed


