class Card extends Payment{
    constructor(id, typeCard, amount){
        super(id);
        this.typeCard = typeCard;
        this.amount = amount;
    }
}