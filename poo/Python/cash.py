from payment import Payment

class Cash(Payment):
    amount = int

    def __init__(self, id, amount):
        super().__init__(id)
        self.amount = amount