class Cidade:
    def __init__(self, nome, distancia_reta):
        self.nome = nome
        self.visitado = False
        self.distancia_reta = distancia_reta
        self.adjacentes = []

    def add_cidade_adjacente(self, cidade):
        self.adjacentes.append(cidade)