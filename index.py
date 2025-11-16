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
    return distancias[:k]
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

def prever_nota(usuario, filme, avaliacoes, k=3):
    vizinhos = vizinhos_proximos(usuario, avaliacoes, k)

    notas = [
        avaliacoes[v][filme]
        for v, _ in vizinhos
        if filme in avaliacoes[v]
    ]

    if filme in avaliacoes[usuario]:
        notas.append(avaliacoes[usuario][filme])

    if not notas:
        return None

    return round(sum(notas) / len(notas), 2)



print("Usuários disponíveis:", ", ".join(avaliacoes.keys()))
usuario_escolhido = input("\nDigite o nome do usuário que você quer analisar: ").strip()

if usuario_escolhido not in avaliacoes:
    print("\n❌ Usuário não encontrado.")
else:
    print("\n===== RESULTADOS PARA:", usuario_escolhido, "=====")

    print("\n🔹 Vizinhos mais próximos:")
    print(vizinhos_proximos(usuario_escolhido, avaliacoes, k=3))

    print("\n🔹 Recomendações de filmes:")
    print(recomendar_filmes(usuario_escolhido, avaliacoes, k=3))

    filme_desejado = input("\nDigite um filme para prever a nota (ex: Duna): ").strip()

    print("\n🔹 Previsão da nota:")
    print(prever_nota(usuario_escolhido, filme_desejado, avaliacoes, k=3))