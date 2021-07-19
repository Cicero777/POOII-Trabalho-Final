from collections import Counter

class PackPOOII():
    """ documentação"""
    def __init__(self):
        pass

    def subString(self, palavra):
        """ documentação"""
        total = 0
        for letras in range(len(palavra)):
            if(palavra[letras: letras+6] == "banana"):
                total += 1
        return total
    

    def deleteLine(self, arq_text, linha):
        """ documentação"""
        with open(arq_text, "r") as f:
            lines = f.readlines()
        with open(arq_text, "w") as f:
            for line in lines:
                if line.strip("\n") != linha:
                    f.write(line)


    def popularidade(self, arq_text, palavras):
        """ documentação"""
        
        palavras = palavras.lower().replace(',', '').split() # tirar virgulas

        lista = []
        with open(arq_text, "r") as f:
            lines = f.readlines()
            line = lines.lower().split()
        with open(arq_text, "r") as f:
            for line in lines:
                for p in palavras:
                    for t in line:
                        if p == t:
                            lista.append(t)
        return Counter(lista) # return quando todas as palavras verificadas

o = PackPOOII()
print(o.deleteLine(input('> '), input('> ')))