# Ejercicio 1 - Práctica de git
# Aportes de: Chris, Luisito y Kene


# --- Chris: Calculadora básica (suma, resta, multiplicación y división) ---
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def calculadora():
    print("=== Calculadora básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1-4): ")

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == "2":
        print(f"Resultado: {restar(a, b)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == "4":
        print(f"Resultado: {dividir(a, b)}")
    else:
        print("Opción no válida")


# --- Luisito el nene ---
def pruebas_luis():
    nombre = "Luis"

    # Mostrar en consola
    print("Hola " + nombre)

    # Condición
    if nombre == "Luis":
        print("Bienvenido")

    # Ciclo
    for i in range(1, 6):
        print(i)

    # Función (reutiliza la suma de la calculadora)
    print(sumar(3, 5))


# --- Kene: Promedios de estudiantes ---
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
    print("hola mucha ponganse a hacer algo")
    print()

    # Aporte de Luisito
    pruebas_luis()
    print()

    # Aporte de Kene
    estudiantes = {
        "Ana": [80, 75, 90],
        "Carlos": [55, 60, 58],
        "Luis": [95, 88, 92],
        "María": [70, 65, 78]
    }
    mostrar_resultados(estudiantes)
    print()

    # Aporte de Chris
    calculadora()


if __name__ == "__main__":
    main()
