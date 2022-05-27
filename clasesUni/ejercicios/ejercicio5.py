#CONSTANTES
#ENTRADA
texto = input("Ingrese un texto cualguiera: ")
#PROCESAMIENTO
texto = texto.lower()
i = 0
texto2 = ""
while(i < len(texto)):
    if(texto[i] != " "):
        texto2 += texto[i]
    i += 1
texto2 = texto2.upper()
#SALIDA
print("Este es el Texto Resultante: ", texto2)
