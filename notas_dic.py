def ingreso_notas():
    """ Esta función retorna un diccionario con los nombres y notas de estudiantes """
    nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre}: "))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
    return dicci

def promedio(dic):
    """ Esta función devuelve el promedio de los valores de un diccionario """
    total = 0
    for elem in dic:
        total = total + dic[elem]
    return total/len(dic)

def debajo_de(dic,valor):
    """ Esta función devuelve las claves de los valores de un diccionario que están por debajo de un valor dado """
    aux = []
    for elem in dic:
        if dic[elem] < valor:
            aux = aux + [elem]
    return aux

notas_de_estudiantes = ingreso_notas()
promedio_notas = promedio(notas_de_estudiantes)
debajo_del_promedio = debajo_de(notas_de_estudiantes,promedio_notas)

print(f"El promedio es {promedio_notas} y {debajo_del_promedio} tienen notas por debajo del mismo.")