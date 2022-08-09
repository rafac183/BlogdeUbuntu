from payment import Payment

class Cash(Payment):
    amount = int
    typeCard = str

    def __init__(self, id, amount, typeCard):
        super().__init__(id)
        self.amount = amount
        self.typeCard = typeCard