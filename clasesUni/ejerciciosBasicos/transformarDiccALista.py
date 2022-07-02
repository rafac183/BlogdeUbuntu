#CTES
dicc = {'fruta': ['plátano', 'manzana'], 'verdura': ['zanahoraria', 'tomate']}
#BLOQUE DE FUNCIONES
#ENTRADA: Diccionario
#SALIDA: Cantidad de llaves y elementos
#CALCULA LA CANTIDAD DE ELEMENTOS EN EL DICCIONARIO
def tabla(diccionario):
    lista2 = []
    for elem in diccionario:
        valores = diccionario[elem]
        for valor in valores:
            lista2.append([valor, elem])
    return lista2
#BLOQUE PRINCIPAL
#ENTRADAS
#txt = input("Texto: ")
#PROCESAMIENTO
resultado = tabla(dicc)
#SALIDA