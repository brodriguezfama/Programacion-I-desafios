import random


def calcular_promedio_alumnos(matriz):
    for t in range(1, len(matriz)):
        notas = 0

        for i in range(1, len(matriz[0])):
            notas += matriz[t][i]

        promedio = notas / i
        print(f"Alumno: {matriz[t][0]} tiene un promedio de: {promedio}")
    print()


def calcular_promedio_materias(matriz):
    for t in range(1, len(matriz[0])):
        notas = 0

        for i in range(1, len(matriz)):
            notas += matriz[i][t]

        promedio = notas / i
        print(f"Materia: {matriz[t][0]} tiene un promedio de: {promedio}")
    print()        


def mostrar_matriz(matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            print(f"{matriz[y][x] : ^10}", end=" ")
        print()


materias = ["Legajo", "mate1", "mate2", "mate3", "mate4"]
estudiantes = [1, 2, 3, 4, 5]
matriz = []
for fil in range(len(estudiantes) + 1):
    matriz.append([])
    for col in range(len(materias)):
        matriz[fil].append(0)

temp = -1

for l in range(len(matriz)):
    for p in range(len(matriz[0])):
        if l == 0:
            matriz[l][p] = materias[p]
        else:
            matriz[l][p] = estudiantes[temp]
    temp += 1

for j in range(1, len(matriz)):
    for i in range(1, len(matriz[0]) - 1):
        matriz[j][i] = random.randint(0, 10)

mostrar_matriz(matriz)
calcular_promedio_alumnos(matriz)
calcular_promedio_materias(matriz)