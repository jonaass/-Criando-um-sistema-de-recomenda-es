import math


avaliacoes = {
    'Jonas': {
        'Matrix': 4.5, 'Avatar': 3.0, 'Titanic': 4.0, 'Interestelar': 5.0,
        'Duna': 4.0, 'Oppenheimer': 4.5
    },
    'Tony': {
        'Matrix': 5.0, 'Avatar': 3.5, 'Titanic': 4.5, 'Interestelar': 4.0,
        'Duna': 5.0, 'Oppenheimer': 4.0, 'John Wick': 4.5
    },
    'Sophia': {
        'Matrix': 4.0, 'Avatar': 2.5, 'Titanic': 4.0, 'Duna': 4.5,
        'Barbie': 4.0, 'John Wick': 3.0
    },
    'Fernanda': {
        'Avatar': 4.5, 'Titanic': 3.0, 'Interestelar': 4.5, 'Duna': 4.0,
        'Oppenheimer': 5.0, 'Barbie': 3.5
    },
    'Marcos': {
        'Matrix': 3.5, 'Avatar': 4.0, 'Titanic': 3.0, 'John Wick': 4.5,
        'Oppenheimer': 3.5, 'Clube da Luta': 5.0
    },
    'Paula': {
        'Matrix': 4.0, 'Titanic': 5.0, 'Interestelar': 4.0, 'Duna': 3.5,
        'Clube da Luta': 4.5, 'Oppenheimer': 4.0
    },
    'Lucas': {
        'Avatar': 3.5, 'Titanic': 3.0, 'John Wick': 5.0, 'Clube da Luta': 4.0,
        'Barbie': 2.5, 'Oppenheimer': 3.0
    },
    'Aline': {
        'Matrix': 4.5, 'Avatar': 4.0, 'Interestelar': 5.0, 'Oppenheimer': 4.0,
        'Barbie': 4.5, 'Clube da Luta': 3.5
    },
    'Diego': {
        'Matrix': 3.0, 'Titanic': 4.0, 'Duna': 4.5, 'John Wick': 4.0,
        'Clube da Luta': 5.0, 'Oppenheimer': 4.0
    },
    'Camila': {
        'Avatar': 4.5, 'Titanic': 5.0, 'Interestelar': 4.5,
        'Barbie': 4.5, 'Duna': 3.5
    }
}

##print(avaliacoes['Jonas']['Matrix'])  

def distancia_euclidiana(usuario1, usuario2, avaliacoes):
    filmes1, filmes2 = avaliacoes[usuario1], avaliacoes[usuario2]
    comuns = set(filmes1).intersection(filmes2)
    if not comuns:
        return None
    return math.sqrt(sum(map(lambda f: (filmes1[f] - filmes2[f]) ** 2, comuns)))

##print("Jonas x Tony =", distancia_euclidiana("Jonas", "Tony", avaliacoes))
##print("Jonas x Sophia =", distancia_euclidiana("Jonas", "Sophia", avaliacoes))
##print("Jonas x Fernanda =", distancia_euclidiana("Jonas", "Fernanda", avaliacoes))


def vizinhos_proximos(usuario, avaliacoes, k=3):
    distancias = []
    for outro in avaliacoes:
        if outro == usuario:
            continue
        d = distancia_euclidiana(usuario, outro, avaliacoes)
        if d is not None:
            distancias.append((outro, d))
    distancias.sort(key=lambda x: x[1])
    return [(nome, round(dist, 2)) for nome, dist in distancias[:k]]
##print("Vizinhos de Jonas:", vizinhos_proximos("Jonas", avaliacoes, k=3))


def recomendar_filmes(usuario, avaliacoes, k=3):
    vizinhos = vizinhos_proximos(usuario, avaliacoes, k)
    notas_usuario = avaliacoes[usuario]
    recomendacoes = {}
    for vizinho, dist in vizinhos:
        for filme, nota in avaliacoes[vizinho].items():
            if filme not in notas_usuario:
                if filme not in recomendacoes:
                    recomendacoes[filme] = []
                recomendacoes[filme].append(nota)
    recomendacoes_finais = {
        filme: sum(notas) / len(notas)
        for filme, notas in recomendacoes.items()
    }
    return sorted(recomendacoes_finais.items(), key=lambda x: x[1], reverse=True)

##print("Recomendações para Jonas:", recomendar_filmes("Jonas", avaliacoes, k=3))

def prever_nota(usuario, filme, avaliacoes, k=3):
    vizinhos = vizinhos_proximos(usuario, avaliacoes, k)
    notas = []
    for vizinho, dist in vizinhos:
        if filme in avaliacoes[vizinho]:
            notas.append(avaliacoes[vizinho][filme])
    if not notas:
        return None
    return sum(notas) / len(notas)

##print("Previsão da nota de Jonas para 'Duna':", prever_nota("Jonas", "Duna", avaliacoes, k=3))


def mostrar_filmes(usuario):
    print(f"\n===== FILMES AVALIADOS POR {usuario} =====")
    for filme, nota in avaliacoes[usuario].items():
        print(f"- {filme}: nota {nota}")
    print("====================================\n")
    

print("Usuários disponíveis:", ", ".join(avaliacoes.keys()))
usuario_escolhido = input("\nDigite o nome do usuário que você quer analisar: ").strip()

if usuario_escolhido not in avaliacoes:

    print("\nUsuário não encontrado.")
    
else:
    print("\n===== RESULTADOS PARA:", usuario_escolhido, "=====")

    print(mostrar_filmes(usuario_escolhido))

    print("\nRecomendações de filmes:")

    print(recomendar_filmes(usuario_escolhido, avaliacoes, k=3))

