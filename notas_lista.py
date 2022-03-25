#Ingresar las notas
nota = int(input("Ingresá una nota (-1 para finalizar): "))
lista_de_notas = []
while nota != -1:
    lista_de_notas.append(nota)
    nota = int(input("Ingresá una nota (-1 para finalizar): "))

#Recorrer lista para calcular el promedio
cant_notas = len(lista_de_notas)
suma = 0
for i in range(cant_notas):
    suma = suma + lista_de_notas[i]
promedio = suma/cant_notas

#Recorrer lista para calcular cuántos tienen notas menores al promedio
total = 0
for i in range(cant_notas):
    if lista_de_notas[i] < promedio:
        total = total + 1

print(f"El promedio de las notas es {promedio} y hay {total} nota/s menor/es al promedio.")