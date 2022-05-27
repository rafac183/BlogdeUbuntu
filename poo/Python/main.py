from ast import If
from json.tool import main
from multiprocessing.spawn import _main
from car import Car #Importar de la clase Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car("AB789", 5, Account("Andres Herrera", "AC456"))
    print(vars(car))
    print(vars(car.driver))

