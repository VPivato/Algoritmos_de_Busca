class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1 # Referencia o topo da pilha, -1 == vazia

    def empilhar(self, cidade):
        if not Pilha.pilha_cheia(self): # Empilha apenas se a pilha não estiver cheia
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("Pilha cheia")

    def desempilhar(self):
        if not Pilha.pilha_vazia(self): # Desempilha apenas se a pilha não estiver vazia
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp
        else:
            print("Pilha vazia")
            return None

    def get_topo(self):
        return self.cidades[self.topo]

    def pilha_vazia(self):
        return self.topo == -1 # Retorna boolean

    def pilha_cheia(self):
        return self.topo == self.tamanho-1 # Retorna boolean, −1 para não dar erro de índice