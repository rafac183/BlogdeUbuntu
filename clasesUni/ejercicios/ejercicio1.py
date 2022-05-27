#VARIABLES
#ENTRADA
edad = input("Ingrese la primera edad: ")
edad2 = input("Ingrese la segunda edad: ")
#PROCESAMIENTO
edad = int(edad)
edad2 = int(edad2)

diferencia = edad - edad2

if(diferencia < 0):
    diferencia *= (-1)

diferencia = str(diferencia)

resultado_final = "Esta es la diferencia de edad: " + diferencia
#SALIDA
print(diferencia)