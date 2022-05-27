#VARIABLES
pi = 3.14
#ENTRADAS
radio = input("Ingrese el Radio del Circulo: ")

#PROCESAMIENTO
radio = float(radio)
area =  pi * (radio**2)
perimetro = 2 * pi * radio

#SALIDA
print("El Area es: ", area, " cm2")
print("El Perimetro es: ", perimetro, "cm")
