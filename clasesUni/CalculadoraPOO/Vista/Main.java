package Vista;
import Controlador.*;
import java.util.*;

public class Main{
    Suma objSuma = new Suma();
    Resta objResta = new Resta();
    Multiplicacion objMultiplicacion = new Multiplicacion();
    Division objDivision = new Division();
    public void main(){
        double a;
        double b;
        Scanner teclado;
        Scanner tecladoOne;
        Scanner tecladoTwo;
        boolean trueValue = true;
        int opcion;
        try {
            System.out.println("Bienvenidos a la Calculadora de POO!\n");

            System.out.println("Ingresa una de las siguientes opciones: \n" 
            + "1° Suma\n" 
            + "2° Resta\n"
            + "3° Multiplicacion\n"
            + "4° Division");
            
            teclado = new Scanner(System.in);
            opcion = teclado.nextInt();
            while(trueValue == true){
                trueValue = false;
                switch (opcion) {
                    case 1:
                        System.out.println("Ingrese el primer numero: ");
                        tecladoOne = new Scanner(System.in);
                        a = tecladoOne.nextDouble();

                        System.out.println("Ingrese el segundo numero: ");
                        tecladoTwo = new Scanner(System.in);
                        b = tecladoTwo.nextDouble();

                        double suma = objSuma.Operar(a, b);

                        System.out.println("\n\nEl resultado de la suma es: " + suma + ".");
                        break;
                    case 2:
                        System.out.println("Ingrese el primer numero: ");
                        tecladoOne = new Scanner(System.in);
                        a = teclado.nextDouble();

                        System.out.println("Ingrese el segundo numero: ");
                        tecladoTwo = new Scanner(System.in);
                        b = tecladoTwo.nextDouble();

                        double resta = objResta.Operar(a, b);

                        System.out.println("\n\nEl resultado de la suma es: " + resta + ".");
                        break;
                    case 3: 
                        System.out.println("Ingrese el primer numero: ");
                        tecladoOne = new Scanner(System.in);
                        a = teclado.nextDouble();

                        System.out.println("Ingrese el segundo numero: ");
                        tecladoTwo = new Scanner(System.in);
                        b = tecladoTwo.nextDouble();

                        double multiplicacion = objMultiplicacion.Operar(a, b);

                        System.out.println("\n\nEl resultado de la suma es: " + multiplicacion + ".");
                        break;
                    case 4:
                        System.out.println("Ingrese el primer numero: ");
                        tecladoOne = new Scanner(System.in);
                        a = tecladoOne.nextDouble();

                        System.out.println("Ingrese el segundo numero: ");
                        tecladoTwo = new Scanner(System.in);
                        b = tecladoTwo.nextDouble();

                        double division = objDivision.Operar(a, b);

                        System.out.println("\n\nEl resultado de la suma es: " + division + ".");
                        break;
                    default:
                        trueValue = true;
                        System.out.println("Error numero equivocado. \nIngrese Otra vez");
                        teclado = new Scanner(System.in);
                        opcion = teclado.nextInt();
                        break;
                }
            }    
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
    
}