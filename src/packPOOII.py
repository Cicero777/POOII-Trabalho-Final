from collections import Counter

class PackPOOII():
    """Aplica métodos para manipulação de texto
    
    """
    def __init__(self):
        pass

    def subString(self, palavra):
        """ Procura uma sub-string dentro de uma determinada string

        Parametros
        ----------
        palavra : str
        Endereço da string 
    
        """
        total = 0
        for letras in range(len(palavra)):
            if(palavra[letras: letras+6] == "banana"):
                total += 1
        return total
    

    def deleteLine(self, arq_text, linha):
        """ Deleta uma linha de um arquivo de texto

        Parametros
        ----------
        arq_text : str
        Nome do arquivo de texto, com a extenção.

        linha : str
        Conteúdo da linha de se deseja excluir 
    
        """
        with open(arq_text, "r") as f:
            lines = f.readlines()
        with open(arq_text, "w") as f:
            for line in lines:
                if line.strip("\n") != linha:
                    f.write(line)


    def popularidade(self, arq_text, palavras):
        """ Retorna quantas vezes uma ou mais palavras aparecem em um arquivo de texto

        Parametros
        ----------
        arq_text : str
        Nome do arquivo de texto, com a extenção

        palavras : str
        Palavras que se deseja obter 
    
        """ 
        palavras = palavras.lower().replace(',', '').split() # tirar virgulas

        lista = []
        with open(arq_text, "r") as f:
            lines = f.readlines()
        with open(arq_text, "r") as f:
            for line in lines:
                texto = line.lower().split()
                for p in palavras:
                    for t in texto:
                        if p == t:
                            lista.append(t)
        return Counter(lista) # return quando todas as palavras verificadas
