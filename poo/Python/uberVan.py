from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, passengers, driver, typeCarAccepted, seatsMaterial) -> None:
        super().__init__(license, passengers, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial