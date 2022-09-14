package Modelo;

public class Operacion
{
    protected double nro1;
    protected double nro2;
    protected double result;

    public Operacion(){}
    public Operacion(double num1, double num2, double resultado){
        this.nro1 = num1;
        this.nro2 = num2;
        this.result = resultado;
    }

    public double getNro1() {
        return nro1;
    }

    public void setNro1(double nro1) {
        this.nro1 = nro1;
    }

    public double getNro2() {
        return nro2;
    }

    public void setNro2(double nro2) {
        this.nro2 = nro2;
    }

    public double getResult() {
        return result;
    }

    public void setResult(double result) {
        this.result = result;
    }
    
}
