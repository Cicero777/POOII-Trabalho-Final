""" 
    O DOS não suporta ANSI diretamente, precisa do driver ANSI.SYS no config.sys 

    device=ANSI.SYS
"""

def cor(palavra, cor):
    cor = cor.upper()
    if cor == "YELLOW":
        pYellow = f"\033[33m{palavra} \033[m"
        return pYellow
    elif cor == "BLACK":
        pBlack = f"\033[30m{palavra} \033[m"
        return pBlack
    elif cor == "RED":
        pRed = f"\033[1;31m{palavra} \033[m"
        return pRed
    elif cor == "BLUE":
        pBlue = f"\033[1;34m{palavra} \033[m"
        return pBlue
    elif cor == "CIAN":
        pCian = f"\033[1;36m{palavra} \033[m"
        return pCian
    elif cor == "GREEN":
        pGreen = f"\033[1;32m{palavra} \033[m"
        return pGreen
    elif cor == "WHITE":
        pWhite = f"\033[37m{palavra} \033[m"
        return pWhite
    else:
        return "Cor não existe"


def printRed(palavra):
    print(f"\033[1;31m{palavra} \033[m")

def printGreen(palavra):
    print(f"\033[1;32m{palavra} \033[m")

def printBlue(palavra):
    print(f"\033[1;34m{palavra} \033[m")

def printCian(palavra):
    print(f"\033[1;36m{palavra} \033[m")

def printWhite(palavra):
    print(f"\033[37m{palavra} \033[m")

def printBlack(palavra):
    print(f"\033[30m{palavra} \033[m")

def printYellow(palavra):
    print(f"\033[33m{palavra} \033[m")


