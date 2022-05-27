#CONSTANTES

#ENTRADA
texto = input("Ingrese un texto: ")

a_1 = 0
e_1 = 0
i_1 = 0
o_1 = 0
u_1 = 0
#PROCESAMIENTO
texto = texto.lower()
i = 0
while(i < len(texto)):
    nro = texto[i]
    if("a" == nro):
        a_1 += 1
    elif("e" == nro):
        e_1 += 1         
    elif("i" == nro):
        i_1 += 1
    elif("o" == nro):
        o_1 += 1
    elif("u" == nro):
        u_1 += 1
    
    i += 1

#SALIDA
print("En el texto hay ", a_1, "Vocales 'a'")
print("En el texto hay ", e_1, "Vocales 'e'")
print("En el texto hay ", i_1, "Vocales 'i'")
print("En el texto hay ", o_1, "Vocales 'o'")
print("En el texto hay ", u_1, "Vocales 'u'")
    
