class Paypal extends Payment{
    constructor(id, amount, email){
        super(id);
        this.amount = amount;
        this.email = email;
    }
}