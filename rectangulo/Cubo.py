from Rectangulo import Rectangulo

class Cubo(Rectangulo):
    def __init__(self, largo, ancho, lado3):
        super().__init__(largo, ancho)
        self.lado3 = lado3

    def volumen(self):
        return self.largo * self.ancho * self.lado3
