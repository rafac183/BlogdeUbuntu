#CONSTANTES
#Titulo
print("Calcular Ecuacion Cuadratica:")
#ENTRADAS
a = input("Ingrese el Valor de 'a': ")
b = input("Ingrese el Valor de 'b': ")
c = input("Ingrese el Valor de 'c': ")
x = input("Ingrese el Valor de 'x': ")
#PROCESAMIENTO
a = int(a)
b = int(b)
c = int(c)
x = int(x)
ec = a*(x)**2 + b*x + c

#SALIDA
print("Resultado: ", ec)