from pilha import Pilha

# Busca sem informação, busca em profundidade
class Profundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(20)
        self.fronteira.empilhar(inicio)
        self.achou = False

    def buscar(self):
        topo = self.fronteira.get_topo()

        if topo == self.objetivo:
            self.achou = True
            print(f"Achou: {topo.nome}")
        else:
            for a in topo.adjacentes: # Percorre todos os adjacentes da cidade que está no topo
                if not self.achou:
                    if not a.cidade.visitado: # Executa apenas se a cidade não foi visitada e se não é o objetivo
                        a.cidade.visitado = True
                        self.fronteira.empilhar(a.cidade)
                        Profundidade.buscar(self) # Recursividade até que todas as cidades sejam visitadas
        self.fronteira.desempilhar()

from mapa import Mapa
mapa = Mapa()
profundidade = Profundidade(mapa.porto_uniao, mapa.curitiba)
profundidade.buscar()