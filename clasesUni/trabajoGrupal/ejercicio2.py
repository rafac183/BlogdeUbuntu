#CONSTANTES
VPORMIN = 350
#Titulo
print("Calcular velocidad a una determinada cantidad de minutos")
#ENTRADA
distancia = input("Ingrese la cantidad de metros recorridos: ")
#min = input("Ingrese la cantidad de minutos recorridos: ")
#PROCESAMIENTO
distancia = int(distancia)
#Determinar si el usuario ingreso un monto menor a 100
incorrect_distance = False
if(distancia < 100):
    incorrect_distance = True
else:
    i = 1
    while(distancia < resultado):
        resultado = VPORMIN * (0.95)**(i-1)

#SALIDA
if(incorrect_distance == True):
    print("ERROR")
    print("NO APLICA")
print(resultado)
