# Programa para calcular el área de un triángulo
# Solicita al usuario la base y la altura, calcula el área y muestra el resultado.
# Autor: Tu nombre

def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

nombre_usuario: str = input("Introduce tu nombre: ")
print(f"\nHola, {nombre_usuario}. Vamos a calcular el área de un triángulo.")

base: float = float(input("Introduce la base del triángulo (en cm): "))
altura: float = float(input("Introduce la altura del triángulo (en cm): "))

area: float = calcular_area_triangulo(base, altura)
es_mayor_a_20: bool = area > 20

print(f"\nEl área del triángulo es: {area:.2f} cm²")
print(f"¿El área es mayor a 20 cm²? {es_mayor_a_20}")

