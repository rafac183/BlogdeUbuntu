import email
from payment import Payment

class Cash(Payment):
    amount = int
    email = str

    def __init__(self, id, amount, email):
        super().__init__(id)
        self.amount = amount
        self.email = email