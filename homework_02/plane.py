"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)  # parent initialization
        self.max_cargo = max_cargo  # parent overriding

    def load_cargo(self, value: int):
        if value + self.cargo > self.max_cargo:
            raise CargoOverload
        self.cargo += value

    def remove_all_cargo(self) -> int:
        temp_val = self.cargo
        self.cargo = 0
        return temp_val
