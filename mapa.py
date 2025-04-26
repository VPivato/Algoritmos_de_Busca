from cidade import Cidade
from adjacente import Adjacente

class Mapa:
    porto_uniao = Cidade("Porto União")
    paulo_frontin = Cidade("Paulo Frontin")
    canoinhas = Cidade("Canoinhas")
    irati = Cidade("Irati")
    palmeira = Cidade("Palmeira")
    campo_largo = Cidade("Campo Largo")
    curitiba = Cidade("Curitiba")
    balsa_nova = Cidade("Balsa Nova")
    araucaria = Cidade("Araucária")
    sao_jose = Cidade("São José dos Pinhais")
    contenda = Cidade("Contenda")
    mafra = Cidade("Mafra")
    tijucas = Cidade("Tijucas do Sul")
    lapa = Cidade("Lapa")
    sao_mateus = Cidade("São Mateus")
    tres_barras = Cidade("Três Barras")

    porto_uniao.add_cidade_adjacente(Adjacente(paulo_frontin))
    porto_uniao.add_cidade_adjacente(Adjacente(canoinhas))
    porto_uniao.add_cidade_adjacente(Adjacente(sao_mateus))

    paulo_frontin.add_cidade_adjacente(Adjacente(irati))
    paulo_frontin.add_cidade_adjacente(Adjacente(porto_uniao))

    canoinhas.add_cidade_adjacente(Adjacente(porto_uniao))
    canoinhas.add_cidade_adjacente(Adjacente(tres_barras))
    canoinhas.add_cidade_adjacente(Adjacente(mafra))

    irati.add_cidade_adjacente(Adjacente(paulo_frontin))
    irati.add_cidade_adjacente(Adjacente(palmeira))
    irati.add_cidade_adjacente(Adjacente(sao_mateus))

    palmeira.add_cidade_adjacente(Adjacente(irati))
    palmeira.add_cidade_adjacente(Adjacente(sao_mateus))
    palmeira.add_cidade_adjacente(Adjacente(campo_largo))

    campo_largo.add_cidade_adjacente(Adjacente(palmeira))
    campo_largo.add_cidade_adjacente(Adjacente(balsa_nova))
    campo_largo.add_cidade_adjacente(Adjacente(curitiba))

    curitiba.add_cidade_adjacente(Adjacente(campo_largo))
    curitiba.add_cidade_adjacente(Adjacente(balsa_nova))
    curitiba.add_cidade_adjacente(Adjacente(araucaria))
    curitiba.add_cidade_adjacente(Adjacente(sao_jose))

    balsa_nova.add_cidade_adjacente(Adjacente(curitiba))
    balsa_nova.add_cidade_adjacente(Adjacente(campo_largo))
    balsa_nova.add_cidade_adjacente(Adjacente(contenda))

    araucaria.add_cidade_adjacente(Adjacente(curitiba))
    araucaria.add_cidade_adjacente(Adjacente(contenda))

    sao_jose.add_cidade_adjacente(Adjacente(curitiba))
    sao_jose.add_cidade_adjacente(Adjacente(tijucas))

    contenda.add_cidade_adjacente(Adjacente(balsa_nova))
    contenda.add_cidade_adjacente(Adjacente(araucaria))
    contenda.add_cidade_adjacente(Adjacente(lapa))

    mafra.add_cidade_adjacente(Adjacente(tijucas))
    mafra.add_cidade_adjacente(Adjacente(lapa))
    mafra.add_cidade_adjacente(Adjacente(canoinhas))

    tijucas.add_cidade_adjacente(Adjacente(mafra))
    tijucas.add_cidade_adjacente(Adjacente(sao_jose))

    lapa.add_cidade_adjacente(Adjacente(contenda))
    lapa.add_cidade_adjacente(Adjacente(sao_mateus))
    lapa.add_cidade_adjacente(Adjacente(mafra))

    sao_mateus.add_cidade_adjacente(Adjacente(palmeira))
    sao_mateus.add_cidade_adjacente(Adjacente(irati))
    sao_mateus.add_cidade_adjacente(Adjacente(lapa))
    sao_mateus.add_cidade_adjacente(Adjacente(tres_barras))
    sao_mateus.add_cidade_adjacente(Adjacente(porto_uniao))

    tres_barras.add_cidade_adjacente(Adjacente(sao_mateus))
    tres_barras.add_cidade_adjacente(Adjacente(canoinhas))