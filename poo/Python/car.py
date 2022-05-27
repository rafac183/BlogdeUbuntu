from lib2to3.pgen2 import driver
from account import Account

class Car:
    id         = int
    license    = str
    driver     = Account("","")
    passengers = int

    def __init__(self, license, passengers, driver) -> None:
        self.license = license
        self.driver = driver
        self.passengers = passengers

    def printDataCar():
        print()