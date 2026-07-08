print ('hola mucha ponganse a hacer algo')


# lUISITO EL NENE

# Variable
nombre = "Luis"

# Mostrar en consola
print("Hola " + nombre)

# Condición
if nombre == "Luis":
    print("Bienvenido")

# Ciclo
for i in range(1, 6):
    print(i)

# Función
def sumar(a, b):
    return a + b

print(sumar(3, 5))

# Kene

def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def mostrar_resultados(estudiantes):
    print("=== Resultados ===")

    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)

        if promedio >= 60:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"Estudiante: {nombre}")
        print(f"Notas: {notas}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Estado: {estado}")
        print("-" * 30)


def main():
    estudiantes = {
        "Ana": [80, 75, 90],
        "Carlos": [55, 60, 58],
        "Luis": [95, 88, 92],
        "María": [70, 65, 78]
    }

    mostrar_resultados(estudiantes)


if __name__ == "__main__":
    main()