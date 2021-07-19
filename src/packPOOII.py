from collections import Counter

class PackPOOII():
    """ documentação"""
    def __init__(self, texto):
        self._texto = texto


    def subString(self, palavra):
        """ documentação"""
        total = 0
        for letras in range(len(palavra)):
            if(palavra[letras: letras+6] == "banana"):
                total += 1
        print(total)
    

    def deleteLine(self, arq_text, linha):
        """ documentação"""
        with open(arq_text, "r") as f:
            lines = f.readlines()
        with open(arq_text, "w") as f:
            for line in lines:
                if line.strip("\n") != linha:
                    f.write(line)


    def popularidade(self, palavras):
        """ documentação"""
        texto = self._texto.lower().split()
        palavras = palavras.lower().replace(',', '').split() # tirar virgulas

        lista = []

        for p in palavras:
            for t in texto:
                if p == t:
                    lista.append(t)
        return Counter(lista) # return quando todas as palavras verificadas

    print(popularidade("Ao nos resolver a esta tarefa, preste nos atenção nos seguintes a nos pontos:", "nos a preste"))