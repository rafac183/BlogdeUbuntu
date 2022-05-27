#VARIABLES
a = 2
b = 3
#ENTRADA
#PROCESAMIENTO

#UNA EXPRESION
c = ((a + b) * (a * b)) + b%a 

#VARIAS EXPRESIONES
d = a + b
a *= b 
b = a - d
d = (d * a) + b
#SALIDA
#DEBE DAR 31
print(c)
print(d)