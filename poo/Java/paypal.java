class Paypal extends Payment{
    String email;

    public Paypal(Integer id, Integer amount, String email){
        super(id, amount);
        this.email = email;
    }
}