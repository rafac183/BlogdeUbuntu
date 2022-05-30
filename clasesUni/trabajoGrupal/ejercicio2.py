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
    min = 0
    resultado = 0
    while(resultado < distancia):
        min += 1
        resultado += VPORMIN *(0.95)**(min-1)
    promedio = resultado / min

    min = str(min)
    promedio = str(promedio)
txt = "Se necesita(n) " + min + "min para alcanzar la distancia Solicitada"
txt2 = "Velocidad Promedio " + promedio + "m/min (Metros por Minutos)"

#SALIDA
if(incorrect_distance == True):
    print("ERROR")
    print("NO APLICA")
elif(incorrect_distance == False):
    print(txt)
    print(txt2)
