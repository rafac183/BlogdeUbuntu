#VARIABLES

#ENTRADAS
nota1 = input("Ingrese sus Notas:\n1._ ")
nota2 = input("2._ ")
nota3 = input("3._ ")

#PROCESAMIENTO
aprobacion = False
nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)

#Calcular promedio
promedio = (nota1 + nota2 + nota3)/3

#Determinar si aprobó o no
if(promedio >= 3.95):
    aprobacion = True

#SALIDA
if(aprobacion == True):
    print("El Alumno Aprobo el Ramo")
else:
    print("El Alumno Reprobo el Ramo")
