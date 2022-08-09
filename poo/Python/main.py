from car import Car #Importar de la clase Car
from account import Account

def main():
    print("Hola Mundo")
    car = Car("AB789", 5, Account("Andres Herrera", "AC456"))
    datos = Car.printDataCar(car)
main()
