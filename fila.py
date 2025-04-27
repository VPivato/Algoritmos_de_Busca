# Implementação do conceito de fila circular
class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numero_elementos = 0

    def enfileirar(self, cidade):
        if not Fila.fila_cheia(self): # Enfileira apenas se não estiver cheia
            if self.fim == self.tamanho-1: # Se o tamanho máximo da fila for atingido
                self.fim = -1 # Reinicia o valor de fim
            self.fim += 1
            self.cidades[self.fim] = cidade # Adiciona ao vetor cidades, na posição fim, o valor cidade
            self.numero_elementos += 1
        else:
            print("Fila está cheia!")

    def desenfileirar(self):
        if not Fila.fila_vazia(self): # Desenfileira apenas se não estiver vazia
            temp = self.cidades[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho: # Se inicio chegar ao tamanho máxima da fila
                self.inicio = 0 # Reinicia seu valor
            self.numero_elementos -= 1
            return temp
        else:
            print("Fila está vazia!")
            return None

    def get_primeiro(self):
        return self.cidades[self.inicio]

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.tamanho