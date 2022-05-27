#CONSTANTES
#ENTRADA
texto = input("Ingrese un Texto Cualguiera: ")
#PROCESAMIENTO
texto = texto.lower()
espacio = 0
i = 0
while (i < len(texto)):
    if(" " == texto[i]):
        espacio += 1
    i += 1  
#SALIDA
print("Cantidad de espacios: ", espacio)
