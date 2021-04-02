from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = None
    fuel = 0.0
    fuel_consumption = 0.0
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __getattr__(self, sample):
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
