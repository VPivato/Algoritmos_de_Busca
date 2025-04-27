from fila import Fila

# Busca sem informação, busca em largura
class Largura:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(20)
        self.fronteira.enfileirar(inicio)
        self.achou = False

    def buscar(self):
        primeiro = self.fronteira.get_primeiro()
        if primeiro == self.objetivo:
            self.achou = True
            print(f"Achou: {primeiro.nome}")
        else:
            self.fronteira.desenfileirar()
            for a in primeiro.adjacentes:
                if not a.cidade.visitado:
                    a.cidade.visitado = True
                    self.fronteira.enfileirar(a.cidade)
            if self.fronteira.numero_elementos > 0:
                Largura.buscar(self)