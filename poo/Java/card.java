class Card extends Payment {
    String typeCard;
    Integer number; 
    Integer cvv;
    Integer date;

    public Card(Integer id, Integer amount, String typeCard, Integer number, Integer cvv, Integer date){
        super(id, amount);
        this.amount = amount;
        this.typeCard = typeCard;
        this.number = number;
        this.cvv = cvv;
        this.date = date;
    }
}
