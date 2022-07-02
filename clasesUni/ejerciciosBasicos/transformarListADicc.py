lista = [["Maria",12],["Camilo",13],["Mario",12],["Marcela",15]]
dicc = {}
for elem in lista:
    nombre = elem[0]
    edad = elem[1]
    if(edad in dicc):
        actValue = dicc[edad]
        actValue.append(nombre)
        dicc[edad] = actValue
    else:
        dicc[edad] = [nombre]
print(dicc)

#OTRA FORMA
#BLOQUE DE FUNCIONES
#ENTRADA: Int
#SALIDA: Diferencia en las 2 entradas
#CALCULA LA CANTIDAD DE ELEMENTOS EN EL DICCIONARIO
def tabla(fruta1, fruta2, fruta3, fruta4, fruta5):
    lista = [[fruta1], [fruta2], [fruta3], [fruta4], [fruta5]]
    dicc = {}
    i = 0
    while(i < len(lista)):
        valores = lista[i]
        for valor in valores:
            if(valor[0] in dicc):
                act_values = dicc[valor[0]]
                act_values.append(valor)
                dicc[valor[0]] = act_values            
            else:
                dicc[valor[0]] = [valor]
        i+=1
    return dicc
#BLOQUE PRINCIPAL
def main():
    #ENTRADAS
    edad1 = input()
    edad2 = input()
    edad3 = input()
    edad4 = input()
    edad5 = input()
    #PROCESAMIENTO
    diccionario = tabla(edad1, edad2, edad3, edad4, edad5)
    #SALIDA
    print("Diccionario: ", diccionario)
main()

#OTRA FORMA 2
#BLOQUE DE FUNCIONES
#ENTRADA: Int
#SALIDA: Diferencia en las 2 entradas
#CALCULA LA CANTIDAD DE ELEMENTOS EN EL DICCIONARIO
def tabla(fruta1, fruta2, fruta3, fruta4, fruta5):
    lista = [fruta1, fruta2, fruta3, fruta4, fruta5]
    dicc = {}
    for elem in lista:
        if(elem[0] in dicc):
            act_values = dicc[elem[0]]
            act_values.append(elem)
            dicc[elem[0]] = act_values            
        else:
            dicc[elem[0]] = [elem]
    return dicc
#BLOQUE PRINCIPAL
def main():
    #ENTRADAS
    edad1 = input()
    edad2 = input()
    edad3 = input()
    edad4 = input()
    edad5 = input()
    #PROCESAMIENTO
    diccionario = tabla(edad1, edad2, edad3, edad4, edad5)
    #SALIDA
    print("Diccionario: ", diccionario)
main()
