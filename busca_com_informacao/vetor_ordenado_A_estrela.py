class VetorOrdenadoAEstrela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.numero_elementos = 0
        self.adjacentes = [None] * self.tamanho

    def inserir(self, adjacente):
        if self.numero_elementos == 0: # Tratamento caso seja a primeira inserção
            self.adjacentes[0] = adjacente
            self.numero_elementos = 1
            return

        posicao = 0
        i = 0
        while i < self.numero_elementos: # Esse while serve para descobrir a posição do item no vetor ordenado
            if adjacente.distancia_A_estrela > self.adjacentes[posicao].distancia_A_estrela: # Se for maior, quer dizer que não pertence àquela posição
                posicao += 1 # Incrementa 1
            i += 1

        for k in range(self.numero_elementos, posicao, -1): # Desloca todos os valores um índice para frente para liberar espaço
            self.adjacentes[k] = self.adjacentes[k - 1]

        self.adjacentes[posicao] = adjacente # Após descobrir a posição e remanejar os valores posteriores, insere o item em seu devido lugar
        self.numero_elementos += 1 # Adiciona um a quantidade de elementos

    def get_primeiro(self):
        return self.adjacentes[0].cidade

    def mostrar(self):
        for i in range(0, self.numero_elementos):
            print(f"{self.adjacentes[i].cidade.nome} - {self.adjacentes[i].distancia_A_estrela}")