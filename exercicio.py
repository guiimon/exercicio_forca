import os
import re
from unicodedata import normalize

def cria_letrinhas(posicoes):
    descoberto = ''
    for i in range(len(posicoes)):
        if posicoes[i][0] in excecoes or posicoes[i][1] == True:
            descoberto += posicoes[i][0]
        else:
            descoberto += '_'
    return descoberto  

def print_forca(tentativas):
    if tentativas >= 6:
        print(" +--+")        
        print(" |  |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("=====")

    elif tentativas == 5:
        print(" +--+")        
        print(" |  |")
        print(" O  |")
        print("    |")
        print("    |")
        print("    |")
        print("=====")
    elif tentativas == 4:
        print(" +--+")        
        print(" |  |")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("    |")
        print("=====")
    elif tentativas == 3:
        print(" +--+")        
        print(" |  |")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("    |")
        print("=====")
    elif tentativas == 2:
        print(" +--+")        
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("    |")
        print("=====")
    elif tentativas == 1:
        print(" +--+")        
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("    |")
        print("=====")
    elif tentativas == 0:
        print(" +--+")        
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("    |")
        print("=====")

def tem_simbolos(texto):
    simbolos = r'[@_!#$%^&*()<>?/|}{~:]'
    return len(list(re.findall(simbolos, texto)))

def tem_simbolos_letra(texto):
    simbolos = r'[@_!#$%^&*()<>?/|}{~:\-]'
    return len(list(re.findall(simbolos, texto)))

def normaliza_simbolos(texto):
    sem_simbolos = normalize('NFKD', texto).encode('ASCII','ignore').decode('ASCII')
    return sem_simbolos


sims = ['sim', 's', 'y', 'yes']
naos = ['nao', 'n', 'no', 'não']
escolha = ''

while escolha not in naos:
    #reset das variaveis necessárias pro jogo
    palavra = " "
    escolha = ''
    excecoes = ' -'
    descoberto = ''
    tentativas = 6
    posicoes = []
    acertadas = []
    erradas = []
    while True:
        print("Escreva a palavra para o jogo da forca: ")
        palavra = input().lower()
        os.system('cls')
        if any(char.isdigit() for char in palavra):
            palavra = ''
            print("*****A palavra não pode conter números*****")
        elif tem_simbolos(palavra) == 0 and len(palavra) >= 3 and len(palavra) <=30:
            break
        elif len(palavra) < 3:
            print("*****O tamanho mínimo das palavras do jogo é 3 caracteres.*****")
        elif len(palavra) > 30:
            print("*****O tamanho máximo das palavras do jogo é 30 caracteres.*****") 
        elif tem_simbolos != 0:
            print("*****O unico simbolo permitido é o Hífen (-)*****")
        
    for char in palavra:
        if char in excecoes:
            posicoes.append([char, True])
            descoberto += char
        else:
            posicoes.append([char, False])
            descoberto += "_"
    
    while tentativas != 0:  
        letra = ''
        while len(letra) != 1 and letra not in acertadas and letra not in erradas:
            print_forca(tentativas)
            if len(erradas) != 0:
                print("Já foram erradas as seguintes letras: "+ ', '.join(erradas) + ".")
            print(f'Temos as seguintes letras {descoberto}, você ainda tem {tentativas} vidas, digite a proxima letra: ')
            letra = input().lower()
            if len(letra) != 1:
                os.system('cls')
                print("*****Escreva exatamente uma letra*****")
            elif tem_simbolos_letra(letra) != 0:
                letra = ''
                os.system('cls')
                print("*****Simbolos não são permitidos*****")
            elif letra.isnumeric():
                letra = ''
                os.system('cls')
                print("*****Numeros não são permitidos*****")
            elif letra in acertadas or letra in erradas:
                letra = ''
                os.system('cls')
                print("*****Essa letra já foi usada, escolha outra*****")
        os.system('cls')
        if normaliza_simbolos(letra) in normaliza_simbolos(palavra):
            acertadas.append(letra)
            for i in range(len(palavra)):
                if normaliza_simbolos(posicoes[i][0]) == letra:
                    posicoes[i][1] = True
        else:
            erradas.append(letra)
            tentativas -= 1
            print("Essa letra não está na palavra! perdeu uma vida.")
        descoberto = cria_letrinhas(posicoes)
        if '_' not in descoberto:
            os.system('cls')
            print(f"Você venceu! a palavra era {palavra}.")
            break
    
    if tentativas == 0:
        os.system('cls')
        print_forca(tentativas)
        print(f"Que pena vc perdeu! a palavra era {palavra}!")
    while escolha not in sims and escolha not in naos:
        print("Jogar Novamente?")
        print("Responda: " + ", ".join(sims) + " para continuar.")
        print("Ou responda: " +  ", ".join(naos) + " para fechar o jogo. ")
        print("Digite a resposta: ", end='')
        escolha = input().lower()
        if escolha not in sims and escolha not in naos:
            os.system('cls')
            print("*****Comando não reconhecido, tente novamente!*****")
        else:
            os.system('cls')