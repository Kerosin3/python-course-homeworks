"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine

class Car(Vehicle):
    engine = None
    
    def set_engine(self,engine: Engine):
        self.engine = engine # accepting engine 