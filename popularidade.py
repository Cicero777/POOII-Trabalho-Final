from collections import Counter

def popularidade (texto, palavras):

    texto = texto.lower().split()
    palavras = palavras.lower().replace(',', '').split() # tirar virgulas

    lista = []

    for p in palavras:
        for t in texto:
            if p == t:
                lista.append(t)
    return Counter(lista) # return quando todas as palavras verificadas

print(popularidade("Ao nos resolver a esta tarefa, preste nos atenção nos seguintes a nos pontos:", "nos a preste"))