from vetor_ordenado_gulosa import VetorOrdenadoGulosa

"""Utiliza apenas da heurística (aproximação) para escolher a desejabilidade de cada nó,
   nesse caso, é a distância em linha reta até o objetivo. Trata-se de uma aproximação,
   e nem sempre retorna o caminho mais curto de fato."""
class BuscaGulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        self.fronteira = None

    def buscar(self, atual):
        atual.visitado = True # Define a cidade atual como visitada

        if atual == self.objetivo: # Verifica se achou o objetivo
            self.achou = True
            print(f"Gulosa: Achou -> {self.objetivo.nome}")
        else:
            self.fronteira = VetorOrdenadoGulosa(len(atual.adjacentes)) # Cria dinamicamente um vetor ordenado em que o tamanho é a quantidade de adjacentes
            for a in atual.adjacentes: # Itera todos os adjacentes da cidade atual
                if not a.cidade.visitado: # Se a cidade não foi visitada
                    a.cidade.visitado = True # Define como visitada
                    self.fronteira.inserir(a.cidade) # Adiciona no vetor ordenado em sua devida posição

            if self.fronteira.get_primeiro() is not None: # Medida de segurança para evitar qualquer erro
                BuscaGulosa.buscar(self, self.fronteira.get_primeiro()) # Recursividade, busca novamente a partir do item mais próximo do objetivo