import math

avaliacoes = {
    'Jonas': {'Matrix': 4.5, 'Avatar': 3.0, 'Titanic': 4.0, 'Interestelar': 5.0},
    'Tony': {'Matrix': 5.0, 'Avatar': 3.5, 'Titanic': 4.5, 'Interestelar': 4.0, 'Duna': 5.0},
    'Sophia': {'Matrix': 4.0, 'Avatar': 2.5, 'Titanic': 4.0, 'Duna': 4.5},
    'Fernanda': {'Avatar': 4.5, 'Titanic': 3.0, 'Interestelar': 4.5, 'Duna': 4.0}
}

##print(avaliacoes['Jonas']['Matrix'])  

def distancia_euclidiana(usuario1, usuario2, avaliacoes):
    filmes_em_comum = []
    for filme in avaliacoes[usuario1]:
        if filme in avaliacoes[usuario2]:
            filmes_em_comum.append(filme)
    if len(filmes_em_comum) == 0:
        return None
    soma = 0
    for filme in filmes_em_comum:
        soma += (avaliacoes[usuario1][filme] - avaliacoes[usuario2][filme]) ** 2
    return math.sqrt(soma)

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

print(vizinhos('Jonas', avaliacoes))