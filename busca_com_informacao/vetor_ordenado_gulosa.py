class VetorOrdenadoGulosa:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.numero_elementos = 0
        self.cidades = [None] * self.tamanho

    def inserir(self, cidade):
        if self.numero_elementos == 0: # Tratamento caso seja a primeira inserção
            self.cidades[0] = cidade
            self.numero_elementos = 1
            return

        posicao = 0
        i = 0
        while i < self.numero_elementos: # Esse while serve para descobrir a posição do item no vetor ordenado
            if cidade.distancia_reta > self.cidades[posicao].distancia_reta: # Se for maior, quer dizer que não pertence àquela posição
                posicao += 1 # Incrementa 1
            i += 1

        for k in range(self.numero_elementos, posicao, -1): # Desloca todos os valores um índice para frente para liberar espaço
            self.cidades[k] = self.cidades[k-1]

        self.cidades[posicao] = cidade # Após descobrir a posição e remanejar os valores posteriores, insere o item em seu devido lugar
        self.numero_elementos += 1 # Adiciona um a quantidade de elementos

    def get_primeiro(self):
        return self.cidades[0]

    def mostrar(self):
        for i in range(0, self.numero_elementos):
            print(f"{self.cidades[i].nome} - {self.cidades[i].distancia_reta}")