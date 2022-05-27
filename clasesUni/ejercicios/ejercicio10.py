#CONSTANTES
#Titulo
print("Cambiar Vocales de una palabra")
#ENTRADAS
txt = input("Ingrese un texto o Una palabra: ")#buen dia
#PROCESAMIENTO
txt = txt.lower()
i = 0
txt2 = ""
while(i < len(txt)):
    ltr = txt[i]
    if(ltr not in 'aeiou'):
        txt2 += ltr
    else:
        ltr=ltr.upper()
        txt2 += ltr
    i += 1
#SALIDA
print("Este es el texto Resultante: ", txt2)