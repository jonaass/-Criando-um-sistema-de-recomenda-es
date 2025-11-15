import math

avaliacoes = {
    'Jonas': {'Matrix': 4.5, 'Avatar': 3.0, 'Titanic': 4.0, 'Interestelar': 5.0},
    'Tony': {'Matrix': 5.0, 'Avatar': 3.5, 'Titanic': 4.5, 'Interestelar': 4.0, 'Duna': 5.0},
    'Sophia': {'Matrix': 4.0, 'Avatar': 2.5, 'Titanic': 4.0, 'Duna': 4.5},
    'Fernanda': {'Avatar': 4.5, 'Titanic': 3.0, 'Interestelar': 4.5, 'Duna': 4.0}
}

##print(avaliacoes['Jonas']['Matrix'])  

def distancia_euclidiana(usuario1, usuario2, avaliacoes):
    filmes1, filmes2 = avaliacoes[usuario1], avaliacoes[usuario2]
    comuns = set(filmes1).intersection(filmes2)
    if not comuns:
        return None
    return math.sqrt(sum(map(lambda f: (filmes1[f] - filmes2[f]) ** 2, comuns)))

##print(distancia_euclidiana('Jonas', 'Tony', avaliacoes))
##print(distancia_euclidiana('Jonas', 'Sophia', avaliacoes))


def vizinhos(usuario, avaliacoes):
    distancias = []
    for outro in avaliacoes:
        if outro != usuario:
            distancia = distancia_euclidiana(usuario, outro, avaliacoes)
            if distancia is not None:
                distancias.append((outro, distancia))
    # Ordena pela menor distância
    distancias.sort(key=lambda x: x[1])
    return distancias

##print(vizinhos('Jonas', avaliacoes))


def recomendar(usuario, avaliacoes, k=2):
    # Encontra os k vizinhos mais próximos
    vizinho = vizinhos(usuario, avaliacoes)[:k]
    
    # Dicionário para somar notas ponderadas
    recomendacoes = {}
    
    for vizinho, distancia in vizinho:
        # Evita divisão por zero
        if distancia == 0:
            continue
        
        for filme in avaliacoes[vizinho]:
            # Só recomenda filmes que o usuário ainda não avaliou
            if filme not in avaliacoes[usuario]:
                # Quanto menor a distância, maior o peso
                peso = 1 / distancia
                if filme not in recomendacoes:
                    recomendacoes[filme] = avaliacoes[vizinho][filme] * peso
                else:
                    recomendacoes[filme] += avaliacoes[vizinho][filme] * peso
    
    # Ordenar por nota (maior primeiro)
    recomendacoes = sorted(recomendacoes.items(), key=lambda x: x[1], reverse=True)
    return recomendacoes

print(recomendar('Jonas', avaliacoes, k=2))

def similaridade_cosseno(usuario1, usuario2, avaliacoes):
    filmes_em_comum = []
    for filme in avaliacoes[usuario1]:
        if filme in avaliacoes[usuario2]:
            filmes_em_comum.append(filme)
    
    if len(filmes_em_comum) == 0:
        return 0
    
    # Produto escalar e magnitude
    numerador = sum(avaliacoes[usuario1][f] * avaliacoes[usuario2][f] for f in filmes_em_comum)
    soma1 = sum(avaliacoes[usuario1][f] ** 2 for f in filmes_em_comum)
    soma2 = sum(avaliacoes[usuario2][f] ** 2 for f in filmes_em_comum)
    
    denominador = math.sqrt(soma1) * math.sqrt(soma2)
    if denominador == 0:
        return 0
    return numerador / denominador
