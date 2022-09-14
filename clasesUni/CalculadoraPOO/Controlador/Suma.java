package Controlador;
import Modelo.*;

public class Suma extends Operacion{
    public double Operar(double x, double y){
        setNro1(x);
        setNro2(y);

        double numberOne = getNro1();
        double numberTwo = getNro2();

        setResult(numberOne + numberTwo);

        double resultado2 = getResult();

        return resultado2;
    }
}