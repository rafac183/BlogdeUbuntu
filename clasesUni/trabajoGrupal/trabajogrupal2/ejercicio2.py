#CTES
lista = [["Maria", 19], ["Mario", 58], ["Camilo", 17], ["Rodolfo", 46]]
#ENTRADAS: Lista
#SALIDA: Numero de registros(int), Diccionario, Edad mayor y menor(int)
#DEFINICION DE FUNCIONES
def registro(lista):
    nombres = []
    edades = []
    edades.sort()
    nro_registros = len(lista)
    for values in lista:
        nombre = values[0]
        edad = values[1]
        nombres.append(nombre)
        edades.append(edad)
    edades.sort()
    for elementos in lista:
        if(edades[0] == elementos[1]):
            minimo = elementos[0]
    edad_menor = edades[0]
    edades.reverse()
    for elementos in lista:
        if(edades[0] == elementos[1]):
            maximo = elementos[0]
    edad_mayor = edades[0]
    dicc = {}
    for nombre in nombres:
        inicial = nombre[0]
        if(inicial in dicc):
            act_values = dicc[inicial]
            act_values.append(nombre)
            dicc[inicial] = act_values
        else:
            dicc[inicial] = [nombre]
    return nro_registros, dicc, minimo, edad_menor, maximo, edad_mayor  
#BLOQUE PRINCIPAL
def main():
    #PROCESAMIENTO
    registro_realizado = registro(lista)
    registros = registro_realizado[0]
    diccionario = registro_realizado[1]
    maximo = registro_realizado[4]
    edad_mayor = registro_realizado[5]
    minimo = registro_realizado[2]
    edad_menor = registro_realizado[3]
    #SALIDA
    print("Numero de registros:", registros)
    print("Diccionario:", diccionario)
    print("Persona mayor", maximo, ":", edad_mayor)
    print("Persona menor", minimo, ":", edad_menor)
main()



