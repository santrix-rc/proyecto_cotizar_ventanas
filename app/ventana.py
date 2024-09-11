class Ventana:
    PRECIOS_ACABADO = {
        'Pulido': 50700,
        'Lacado Brillante': 54200,
        'Lacado Mate': 53600,
        'Anodizado': 57300
    }
    PRECIOS_VIDRIO = {
        'Transparente': 8.25,
        'Bronce': 9.15,
        'Azul': 12.75
    }
    PRECIO_ESMERILADO = 5.20
    PRECIO_CHAPA = 16200
    PRECIO_ESQUINA = 4310

    def __init__(self, ancho, alto, estilo, vidrio, esmerilado=False):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.vidrio = vidrio
        self.esmerilado = esmerilado

    def calcular_costo(self):
        area_vidrio = (self.ancho - 3) * (self.alto - 3)  # Descontando bordes de 1.5cm por cada lado
        costo_vidrio = area_vidrio * self.PRECIOS_VIDRIO[self.vidrio]
        if self.esmerilado:
            costo_vidrio += area_vidrio * self.PRECIO_ESMERILADO

        # Suponiendo que el aluminio es 'Pulido' para este ejemplo
        perimetro_aluminio = 2 * (self.ancho + self.alto)
        costo_aluminio = perimetro_aluminio * self.PRECIOS_ACABADO['Pulido'] / 100

        costo_total = costo_vidrio + costo_aluminio + self.PRECIO_ESQUINA * 4

        if 'X' in self.estilo:
            costo_total += self.PRECIO_CHAPA

        return costo_total

    def __str__(self):
        return (f"Ventana {self.estilo}, {self.ancho}x{self.alto} cm, vidrio {self.vidrio} "
                f"{'esmerilado' if self.esmerilado else ''}. Costo calculado: {self.calcular_costo():.2f}")
