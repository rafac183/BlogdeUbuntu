#CONSTANTES
KGNARANJAS = 750
KGMANZANAS = 1000
KGPERAS = 700
#ENTRADA
naranjas = input("Ingrese los Kg de Naranjas: ")
manzanas = input("Ingrese los Kg de Manzanas: ")
peras = input("Ingrese los Kg de Peras: ")
#PROCESAMIENTO
naranjas = int(naranjas)
manzanas = int(naranjas)
peras = int(peras)

totalNaranjas = naranjas * KGNARANJAS
totalManzanas = manzanas * KGMANZANAS
totalPeras = peras * KGPERAS

gastoTotal = totalNaranjas + totalManzanas + totalPeras

#SALIDA
print("El gasto total es: ", gastoTotal)
