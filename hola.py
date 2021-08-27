print("Aca empieza mi programa -----------------------------------------------------------------Aca empieza mi programa")
#asi se crea una variable
miVar = 10
#asi se guarda en una var la pocion de memoria de una variable
pos = id(miVar)
#asi python imprime en consola una variable
print(miVar)
print(pos)
#asi se crea una variable de texto
miVar2 = "Grupo 29"
print(miVar2)
#asi python imprime cualquier texto
print("Cualquier texto")
print("Aca termina mi programa ---------------------------------")

def controladoPorEventoWhile():
    promedio, total, contar = 0.0,0,0
    print("introduzca la nota de un estudiante (-1 para salir):")
    grado = int(input())
    while grado != -1:
        total = total + grado
        contar = contar + 1
        print("introduzca la nota de un estudiante (-1 para salir):")
        grado = int(input())
    else: 
        promedio = total / contar
        print("promedio de notas del estudiante escolar es: " + str(promedio))

controladoPorEventoWhile()
