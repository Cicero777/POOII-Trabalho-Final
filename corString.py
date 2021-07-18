""" 
    O DOS não suporta ANSI diretamente, precisa do driver ANSI.SYS no config.sys 

    device=ANSI.SYS
"""


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

def green(palavra):
    pGreen = f"\033[1;32m{palavra} \033[m"
    return pGreen

def red(palavra):
    pRed = f"\033[1;31m{palavra} \033[m"
    return pRed

def blue(palavra):
    pBlue = f"\033[1;34m{palavra} \033[m"
    return pBlue

def cian(palavra):
    pCian = f"\033[1;36m{palavra} \033[m"
    return pCian

def white(palavra):
    pWhite = f"\033[37m{palavra} \033[m"
    return pWhite

def black(palavra):
    pBlack = f"\033[30m{palavra} \033[m"
    return pBlack

def yellow(palavra):
    pYellow = f"\033[33m{palavra} \033[m"
    return pYellow

