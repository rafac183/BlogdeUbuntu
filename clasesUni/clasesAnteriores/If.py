#VARIABLES

#ENTRADAS
nro = input("Ingrese un Numero: ")

#PROCESAMIENTO
nro = int(nro)
par_o_impar = False
positivo = False
negativo = False
neutro = False

#Determino si el Numero es par o impar
if(nro%2 == 0):
    par_o_impar = True

#Determino el Signo del numero
if(nro > 0):
    positivo = True
elif(nro == 0):
    neutro = True
elif(nro < 0):
    negativo = True

#SALIDA
if(par_o_impar == True):
    print("El Numero es Par")
else:
    print("El Numero es Impar")

if(positivo == True):
    print("El Numero es Positivo")
elif(neutro == True):
    print("El Numero es Neutro")
elif(negativo == True):
    print("El Numero es Negativo")
