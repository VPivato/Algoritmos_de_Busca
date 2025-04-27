class Adjacente:
    def __init__(self, cidade, distancia_estrada):
        self.cidade = cidade
        self.distancia_estrada = distancia_estrada
        self.distancia_A_estrela = self.cidade.distancia_reta + distancia_estrada
