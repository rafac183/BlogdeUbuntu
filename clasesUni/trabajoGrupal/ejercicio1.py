#ENTRADAS
userName = input("Ingrese su Correo:")

#PROCESAMIENTO
#Transformar a Minusculas
userName = userName.lower()

#Sprint con los Numeros Basicos
num = '0123456789'

#Variable Boleano Inicializado en TRUE para suponer q inicia sin Numero
sinNro = True

#Ciclo For-In que cambie la variable a falso cuando encuentre un Numero
for carac in userName:
    if(carac in num):
        sinNro = False

#Aplicacion de las Reglas
while((len(userName) < 8) or (userName[0] in num) or (' ' in userName) or (sinNro == True)):
    #Si no se cumple alguna de estas reglas no saldra del ciclo
    print("No Cumple con algun Criterio:\n-Largo Minimo 8\n-Existencia de almenos un Digito\n-No deben existir Espacios\n-El Digito no debe estar al Inicio del nombre de usuario")
    userName = input("Por Favor ingrese nuevamente el nombre de usuario:")
    #Misma variable declarada anteriormente para cambiarlo a TRUE si encontro un numero pero no se cumplio alguna condicion
    sinNro = True
    #Mismo Ciclo For-In
    for carac in userName:
        if(carac in num):
            sinNro = False
#Cuando se cumpla el Ciclo lo guardara en esta variable 
txt = userName+"@tucorreo.cl"
#SALIDA
#Imprimir lo Guardado
print(txt)