class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo\n");//Print en Java

        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123", "a.herrera@gmail.com"), "Chevrolet", "Spark"); //Guardar datos en clases de otro archivo
        //uberX.passengers = 5;//como passengers esta en privado no lo muestra en otro paquete
        uberX.setPassengers(5);
        uberX.printDataCar();//Llamar funcion de otro archivo

        //Car car2 = new Car("AMQ456", 2, new Account("Yxzandra Giron", "AND456", "y.giron@gmail.com") ); //Guardar datos en clases de otro archivo
        //car2.printDataCar();
    }
}