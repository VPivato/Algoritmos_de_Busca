from mapa import Mapa

# Busca sem informação
from profundidade import Profundidade
from largura import Largura

"""Busca sem informação: Não é recomendável utilizar para buscar a rota entre duas cidades, por exemplo.
   Mais usado em cenários onde se precise percorrer todos os nós de um grafo, ou verificar se um nó existe.
   Busca em profundidade, busca em largura."""

if __name__ == "__main__":
    mapa = Mapa()

    # Busca sem informação
    profundidade = Profundidade(mapa.porto_uniao, mapa.curitiba) # Profundidade(inicio, final)
    largura = Largura(mapa.porto_uniao, mapa.curitiba) # Largura(inicio, final)