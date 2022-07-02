lista = [15, 10, 2, 100, 1000, 12, 13, 111, 99, 901, 8721, 10278, 19, 17, 20528]
nro_min = 0
nro_max = 0
promedio = 0
lista.sort()
i = 0 
while(i < len(lista)):
    promedio += lista[i]
    if(i == 0):
        nro_min = lista[0]
    else:
        nro_max = lista[i]
    i += 1
'''for carac in lista:
    promedio += carac
    if(nro_max < carac):
        nro_max = carac
        nro_min = carac
for ltr in lista:
    if(nro_min > ltr):
        nro_min = ltr'''
promedio /= len(lista) 
print(nro_min)    
print(nro_max)
print(promedio)
