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

print(vizinhos('Jonas', avaliacoes))