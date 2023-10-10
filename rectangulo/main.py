from Rectangulo import Rectangulo
from Cubo import Cubo

# Solicitar al usuario los datos para el rectángulo
largo_rectangulo = float(input("Ingrese la longitud del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))

# Crear un objeto Rectangulo con los datos proporcionados por el usuario
rectangulo = Rectangulo(largo_rectangulo, ancho_rectangulo)

# Solicitar al usuario los datos para el cubo
largo_cubo = float(input("Ingrese la longitud del cubo: "))
ancho_cubo = float(input("Ingrese el ancho del cubo: "))
lado3_cubo = float(input("Ingrese el tercer lado del cubo: "))

# Crear un objeto Cubo con los datos proporcionados por el usuario
cubo = Cubo(largo_cubo, ancho_cubo, lado3_cubo)

# Mostrar la información de ambos objetos
print("\nInformación del rectángulo:")
rectangulo.ver()

print("\nInformación del cubo:")
cubo.ver()
print(f"Volumen del cubo: {cubo.volumen()}")