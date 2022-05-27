#CONSTANTES
#ENTRADA
nro = input("Ingrese un Numero: ")
#PROCESAMIENTO
nro = int(nro)
resultado = 0
i = 1
while(i <= nro):
    resultado += i 
    i += 2
#SALIDA
print(resultado)