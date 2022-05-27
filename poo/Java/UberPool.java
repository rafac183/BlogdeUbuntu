class UberPool extends Car{
    String brand;
    String model;

    public UberPool(String license, Integer passengers, Account driver, String brand, String model) {
        super(license, passengers, driver);
        this.brand = brand;
        this.model = model;
    }
}
