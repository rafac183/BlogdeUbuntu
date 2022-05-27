#CONSTANTES
#ENTRADA
nro = input("Ingrese un Numero: ")
#PROCESAMIENTO
nro = int(nro)
primo = True
i = 2
while(i < nro):
    if (nro%i == 0):
        primo = False
    i+=1
#SALIDA
if (primo == False):
    print("Este Numero no es primo")
else:
    print("Este Numero es primo")

#CONSTANTES
#ENTRADA
nro = input("Ingrese un Numero: ")
#PROCESAMIENTO
nro = int(nro)
primo = False
i = 1
divisibles = 0
while(i <= nro):
    if(nro%i == 0):
       divisibles += 1 
    i += 1
if(divisibles == 2):
    primo = True
#SALIDA
if(primo == True):
    print("El Numero es Primo")
else:
    print("El Numero no es Primo")
