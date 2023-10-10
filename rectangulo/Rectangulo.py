class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def area(self):
        return self.largo * self.ancho

    def ver(self):
        print(f"Longitud: {self.largo}")
        print(f"Ancho: {self.ancho}")
        print(f"Perímetro: {self.perimetro()}")
        print(f"Área: {self.area()}")
