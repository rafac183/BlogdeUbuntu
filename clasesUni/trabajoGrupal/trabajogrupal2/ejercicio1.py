#ENTRADA: Texto
#SALIDA: Orden de las palabras que mas se repiten o ERROR
#DEFINICION DE FUNCIONES
def min_the_word (texto_ingresado):
    min_valido = True
    min_ltr_valido = True
    texto = texto_ingresado.split(" ")
    texto.sort()
    if(len(texto) < 10):
        min_valido = False
    lista = []
    i = 0
    while(i < len(texto)):
        nro_veces = texto.count(texto[i])
        lista.append([texto[i], nro_veces])
        i += nro_veces 
    if(len(lista) < 4):
        min_ltr_valido = False
    dicc = {}
    i = 0
    while(i < len(lista)):
        nro = lista[i]
        numero = nro[1]
        word = nro[0]
        if(numero not in dicc):
            dicc[numero] = [word]
        else:
            act_values = dicc[numero]
            act_values.append(word)
            dicc[numero] = act_values
        i += 1
    
    return min_valido, min_ltr_valido, dicc
def orden(diccionario):
    llaves = list(diccionario.keys())
    llaves.sort()
    llaves.reverse()
    i = 0
    lugar = 1
    while(i < len(llaves)):
        j = 0
        palabras = ""
        values_in_dicc = diccionario[llaves[i]]
        while(j < len(values_in_dicc)):
            word = values_in_dicc[j]
            palabras += "'" + word + "'" + " "
            j += 1
        print(lugar, "°", palabras, ":", llaves[i])
        lugar += 1
        i += 1
    if(i == 1):
        print(lugar, "°", "No existe")
        lugar += 1
    if(i == 2):
        print(lugar, "°", "No existe")
#BLOQUE PRINCIPAL
def main():
    #ENTRADAS
    txt = input("Ingrese un Texto: ")
    #PROCESAMIENTO
    txt_min_and_list = min_the_word(txt)
    cant_min = True
    cant_words = True
    #SALIDA
    if(txt_min_and_list[0] == False):
        print("ERROR: No se cumple con la cantidad minima de palabras")
        cant_min = False
    if(txt_min_and_list[1] == False):
        print("ERROR: No se cumple con la cantidad minima de palabras distintas")
        cant_words = False
    if(cant_min == True and cant_words == True):
        orden1 = orden(txt_min_and_list[2])
main()