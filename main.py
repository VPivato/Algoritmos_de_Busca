from mapa import Mapa

# Busca sem informação
from profundidade import Profundidade
from largura import Largura

# Busca com informação
from busca_gulosa import BuscaGulosa
from busca_A_estrela import BuscaAEstrela

"""Busca sem informação: Não é recomendável utilizar para buscar a rota entre duas cidades, por exemplo.
   Mais usado em cenários onde se precise percorrer todos os nós de um grafo, ou verificar se um nó existe.
   Busca em profundidade, busca em largura."""

"""Busca com informação: Avalia o grau de 'desejabilidade' de cada nó com base eem uma função heurística.
   Segue expandido com base no nó mais desejável."""

if __name__ == "__main__":
    """Só é possível executar uma busca por vez, provavelmente há algum conflito no atributo 'visitado',
       pois ele não é definido para False novamente após o término de uma busca."""
    mapa = Mapa()

    # Busca sem informação
    profundidade = Profundidade(mapa.porto_uniao, mapa.curitiba) # Profundidade(inicio, final)
    #profundidade.buscar()

    largura = Largura(mapa.porto_uniao, mapa.curitiba) # Largura(inicio, final)
    #largura.buscar()

    # -------------------------------------------------------------------------- #

    # Busca com informação
    busca_gulosa = BuscaGulosa(mapa.curitiba) # BuscaGulosa(final)
    #busca_gulosa.buscar(mapa.porto_uniao) # BuscaGulosa.buscar(inicio)

    busca_A_estrela = BuscaAEstrela(mapa.curitiba)
    #busca_A_estrela.buscar(mapa.porto_uniao)