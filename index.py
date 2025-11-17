import math
import tkinter as tk
from tkinter import ttk, messagebox

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



def distancia_euclidiana(usuario1, usuario2, avaliacoes):
    filmes1, filmes2 = avaliacoes[usuario1], avaliacoes[usuario2]
    comuns = set(filmes1).intersection(filmes2)
    if not comuns:
        return None
    return math.sqrt(sum(map(lambda f: (filmes1[f] - filmes2[f]) ** 2, comuns)))


def recomendar(usuario):
    distancias = []

    for outro in avaliacoes:
        if outro != usuario:
            d = distancia_euclidiana(usuario, outro, avaliacoes)
            if d is not None:
                distancias.append((outro, round(d, 2)))

    distancias.sort(key=lambda x: x[1])
    vizinhos = distancias[:3]
    filmes_usuario = set(avaliacoes[usuario].keys())
    recomendacoes = {}

    for vizinho, _ in vizinhos:
        for filme, nota in avaliacoes[vizinho].items():
            if filme not in filmes_usuario:
                if filme not in recomendacoes:
                    recomendacoes[filme] = []
                recomendacoes[filme].append(nota)

    recomendacoes_finais = [
        (filme, round(sum(notas)/len(notas), 2))
        for filme, notas in recomendacoes.items()
    ]

    recomendacoes_finais.sort(key=lambda x: x[1], reverse=True)
    return vizinhos, recomendacoes_finais



def prever_nota(usuario, filme):
    distancias = []

    for outro in avaliacoes:
        if outro != usuario:
            d = distancia_euclidiana(usuario, outro, avaliacoes)
            if d is not None:
                distancias.append((outro, round(d, 2)))

    distancias.sort(key=lambda x: x[1])
    vizinhos = distancias[:3]

    notas = []
    for vizinho, _ in vizinhos:
        if filme in avaliacoes[vizinho]:
            notas.append(avaliacoes[vizinho][filme])

    if not notas:
        return None

    return round(sum(notas)/len(notas), 2)


def mostrar_filmes(usuario):
    print(f"\n===== FILMES AVALIADOS POR {usuario} =====")
    for filme, nota in avaliacoes[usuario].items():
        print(f"- {filme}: nota {nota}")
    print("====================================\n")
    

def mostrar_resultados():
    usuario = entrada_usuario.get()

    if usuario not in avaliacoes:
        messagebox.showerror("Erro", "Usuário não encontrado!")
        return

    vizinhos, recomendacoes = recomendar(usuario)

    texto_resultado.delete("1.0", tk.END)

    texto_resultado.insert(tk.END, f"===== Resultados para o usuário: {usuario} =====\n\n")

    texto_resultado.insert(tk.END, "Filmes avaliados pelo usuário:\n")
    for filme, nota in avaliacoes[usuario].items():
        texto_resultado.insert(tk.END, f"• {filme}: {nota}\n")

    texto_resultado.insert(tk.END, "\nVizinhos mais próximos:\n")
    for v, d in vizinhos:
        texto_resultado.insert(tk.END, f"• {v}: distância {d}\n")

    texto_resultado.insert(tk.END, "\nRecomendações de filmes:\n")
    for filme, nota in recomendacoes:
        texto_resultado.insert(tk.END, f"• {filme}: nota estimada {nota}\n")

janela = tk.Tk()
janela.title("Sistema de Recomendação de Filmes")
janela.geometry("600x500")

titulo = tk.Label(janela, text="Recomendação de Filmes", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

frame = tk.Frame(janela)
frame.pack(pady=5)

label_usuario = tk.Label(frame, text="Digite o nome do usuário:")
label_usuario.pack(side="left")

entrada_usuario = tk.Entry(frame, width=20)
entrada_usuario.pack(side="left", padx=5)

botao = tk.Button(janela, text="Mostrar Recomendações", command=mostrar_resultados)
botao.pack(pady=10)

texto_resultado = tk.Text(janela, height=20, width=70, font=("Arial", 11))
texto_resultado.pack(pady=10)

janela.mainloop()

##print("Usuários disponíveis:", ", ".join(avaliacoes.keys()))
##usuario_escolhido = input("\nDigite o nome do usuário que você quer analisar: ").strip()

##if usuario_escolhido not in avaliacoes:

##    print("\nUsuário não encontrado.")

##else:
##    print("\n===== RESULTADOS PARA:", usuario_escolhido, "=====")

 ##   print(mostrar_filmes(usuario_escolhido))

 ##   print("\nRecomendações de filmes:")

  ##  print(recomendar_filmes(usuario_escolhido, avaliacoes, k=3))