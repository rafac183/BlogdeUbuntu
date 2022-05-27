class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");//Print en Java

        Car car = new Car("AMQ123", 5, new Account("Andres Herrera", "AND123", "a.herrera@gmail.com") ); //Guardar datos en clases de otro archivo
        car.printDataCar();//Llamar funcion de otro archivo

        Car car2 = new Car("AMQ456", 2, new Account("Yxzandra Giron", "AND456", "y.giron@gmail.com") ); //Guardar datos en clases de otro archivo
        car2.printDataCar();
    }
}