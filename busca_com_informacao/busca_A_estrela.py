from .vetor_ordenado_A_estrela import VetorOrdenadoAEstrela

"""Utiliza tanto a distância em linha reta, quanto a distância pela estrada para calcular
   o nó mais desejável. Essa é a unica diferença em relação a busca gulosa"""
class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        self.fronteira = None

    def buscar(self, atual):
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
            print(f"A Estrela: Achou -> {self.objetivo.nome}")
        else:
            self.fronteira = VetorOrdenadoAEstrela(len(atual.adjacentes))
            for a in atual.adjacentes:
                if not a.cidade.visitado:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            if self.fronteira.get_primeiro() is not None:
                BuscaAEstrela.buscar(self, self.fronteira.get_primeiro())
