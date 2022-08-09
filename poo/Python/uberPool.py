from car import Car

class UberPool(Car):
    brand = str
    model = str

    def __init__(self, license, passengers, driver, brand, model) -> None:
        super().__init__(license, passengers, driver)
        self.brand = brand
        self.model = model