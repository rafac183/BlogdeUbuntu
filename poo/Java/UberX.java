class UberX extends Car {
    String brand;//Atributos de ubeX nada mas
    String model;

    public UberX(String license, Account driver, String brand, String model) {
        super(license, driver);//Referirse al metodo contructor de la clase padre
        this.brand = brand;
        this.model = model;
    }
}
