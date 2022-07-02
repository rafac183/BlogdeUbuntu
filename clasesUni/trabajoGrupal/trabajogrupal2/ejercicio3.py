#CTES
ALUMNOS={"A":[["Andrea Fuentes", "futbol"], ["Andres mendoza", "futbol"], ["Amanda Pinilla", "karate"], ["Andrés Villalobos", "basquetball"]], "R": [["Ricardo Esparza", "escalada"]],"V":[["Vanessa Alguerno", "escalada"]]}
#ENTRADA: Diccionario
#SALIDA: Depende de lo que seleccione el usuario
#DEFINICION DE FUNCIONES
def agregar_new_name (nombre, deporte):    
    #Inicial del nombre
    ltr_inicial = nombre[0]
    #Pregunta si la inicial del nombre esta en el diccionario
    if(ltr_inicial in ALUMNOS):
        #Guarda el valor actual del diccionario 
        act_values = ALUMNOS[ltr_inicial]
        #Añade el nuevo nombre
        name_and_deport = [nombre, deporte]
        act_values.append(name_and_deport)
        #Actualiza el diccionario
        ALUMNOS[ltr_inicial] = act_values
    #Si no esta la inicial, solo lo agrega a la lista
    else:
        #Pero primero lo transformamos en lista
        name_and_deport = [nombre, deporte]
        ALUMNOS[ltr_inicial] = [name_and_deport]
def lista_names_deports():
    #Lista para guardar los nombres actuales y el añadido
    nombres = []
    deporte = []
    #Ahora a recorrer el diccionario actualizado
    #Recorre las iniciales primero
    for names in ALUMNOS:
        #Aqui defino las listas dentro de la inicial
        valores = ALUMNOS[names]
        #recorre las listas del diccionario y las lista de lista
        for valor in valores:
            #Para luego guardar en la lista nueva
            nombres.append(valor[0])
            deporte.append(valor[1])
    nombres.sort()
    deporte.sort()
    return nombres, deporte
#BLOQUE PRINCIPAL
def main():
    #TITULO
    print("¿Que opción desea realizar?\n a)Agregar nuevo alumno\n b)Indicar la cantidad total de alumnos\n c)Indicar la cantidad de alumnos, por cada deporte\n d)Eliminar los alumnos cuyo nombre empiece con cierta letra\n e)Salir")
    #ENTRADAS
    opcion = input("Opción: ")
    #PROCESAMIENTO Y LAS DISTINTAS SALIDAS
    while(opcion not in "Ee"):
        if(opcion in "Aa"):
            #Pedir nombre al usuario
            name = input("Ingrese el Nombre: ")
            #Aqui pasamos la primera letra a mayuscula para el diccionario
            name2 = name[0].upper()
            i = 1
            while(i < len(name)):
                name2 += name[i]
                i += 1
            #Pedir deporte que practica
            deport = input("Ingrese su Deporte: ")
            #Actualizar Diccionario y listas
            act_dicc = agregar_new_name(name2, deport)
            act_list = lista_names_deports()
            #Imprimir los alumnos anotados en el sistema
            #Alumnos en el sistema uno por uno
            names_in_list = lista_names_deports()[0]
            i = 0
            print("Alumnos:")
            while(i < len(names_in_list)):
                print("- ", names_in_list[i])
                i += 1
            #print("¿Que opción desea realizar?\n a)Agregar nuevo alumno\n b)Indicar la cantidad total de alumnos\n c)Indicar la cantidad de alumnos, por cada deporte\n d)Eliminar los alumnos cuyo nombre empiece con cierta letra\n e)Salir")
        elif(opcion in "Bb"):
            #Contar cantidad de alumnos en el sistema
            names_in_list = lista_names_deports()[0]
            cant_alum = len(names_in_list)
            print("Cantidad total de alumnos: ", cant_alum)
#            print("¿Que opción desea realizar?\n a)Agregar nuevo alumno\n b)Indicar la cantidad total de alumnos\n c)Indicar la cantidad de alumnos, por cada deporte\n d)Eliminar los alumnos cuyo nombre empiece con cierta letra\n e)Salir")
        elif(opcion in "Cc"):
            #Cantidad de alumnos por cada deporte
            deports_in_list = lista_names_deports()[1]
            print("Cantidad de alumnos por cada deporte:")
            i = 0
            #Recorrer la lista de deportes para imprimir la candidad de veces que se repite
            while(i < len(deports_in_list)):
                nro = deports_in_list.count(deports_in_list[i])
                nro_repetido = nro
                #Eliminar las veces que se repite la palabra
                while(nro_repetido > 1):
                    deports_in_list.pop(i+1)
                    nro_repetido -= 1
                nro_deportes = "- " + deports_in_list[i] + ":"
                print(nro_deportes, nro)
                i += 1
#            print("¿Que opción desea realizar?\n a)Agregar nuevo alumno\n b)Indicar la cantidad total de alumnos\n c)Indicar la cantidad de alumnos, por cada deporte\n d)Eliminar los alumnos cuyo nombre empiece con cierta letra\n e)Salir")
        elif(opcion in "Dd"):
            print("Las iniciales disponibles son: ",)
            #Recorrer las iniciales disponibles para borrar
            for llave in ALUMNOS:
                print("- ", llave)
            ltr = input("¿Cual letra desea elegir?: ")
            ltr_valida = False
            #Mientras la inicial no se encuentre en el diccionario lanzara error
            while(ltr_valida == False):
                #Pasamos la letra a mayusculas para no encontrar errores
                ltr = ltr.upper()
                #Aplicamos las reglas de eliminado de diccionario
                if(len(ltr) == 1 and ltr in ALUMNOS):
                    nro_eliminados = len(ALUMNOS[ltr])
                    del ALUMNOS [ltr]
                    ltr_valida = True
                else:
                    print("ERROR: Valor ingresado no valido")
                    ltr = input("¿Cual letra desea elegir?: ")
            #Actualizamos la lista
            act_list = lista_names_deports()
            #Alumnos actuales
            alum_act = len(act_list[0])
            print("Fueron Eliminados", nro_eliminados, "Alumnos.")
            print("Permanecen", alum_act, "en el sistema")
            #print("¿Que opción desea realizar?\n a)Agregar nuevo alumno\n b)Indicar la cantidad total de alumnos\n c)Indicar la cantidad de alumnos, por cada deporte\n d)Eliminar los alumnos cuyo nombre empiece con cierta letra\n e)Salir")
        else:
            print("ERROR: Opción no Válida")
        #Siempre preguntar la opcion
        opcion = input("Opción: ")
main()