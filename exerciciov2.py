import os
import re
from unicodedata import normalize
import random


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

def seleciona_palavra():
    tema = random.randint(0, 3)
    palavra = random.randint(0, 9)
    resposta = []
    animais = ["Macaco","Camelo","Cavalo-marinho","Cavalo","Chimpanzé","Arara","Hipopótamo","Elefante","Peixe-Boi","Piranha"]
    lugares = ["Estados Unidos","China","Marrocos","África","Japão","Bolivia","Argentina","Brasil","França","Peru"]
    verbos = ["Andar","Correr","Voar","Balançar","Nadar","Viajar","Fugir","Assassinar","Deitar","Dormir"]
    objetos = ["Banana","Maçã","Cadeira","Dado","Boneco","Carro","Torneira","Ônibus","Balanço","Britadeira"]
    if tema == 0:
        resposta.append("Animal")
        resposta.append(animais[palavra])
    elif tema == 1:
        resposta.append("País")
        resposta.append(lugares[palavra])
    elif tema == 2:
        resposta.append("Verbo")
        resposta.append(verbos[palavra])
    elif tema == 3:
        resposta.append("Objeto")
        resposta.append(objetos[palavra])
    return resposta

sims = ['sim', 's', 'y', 'yes']
naos = ['nao', 'n', 'no', 'não']
escolha = ''

while escolha not in naos:
    #reset das variaveis necessárias pro jogo
    escolha = ''
    excecoes = ' -'
    descoberto = ''
    tentativas = 6
    posicoes = []
    acertadas = []
    erradas = []
    selecao = seleciona_palavra()
    tema = selecao[0]
    palavra = selecao[1]

    for char in palavra:
        if char in excecoes:
            posicoes.append([char, True])
            descoberto += char
        else:
            posicoes.append([char, False])
            descoberto += "_"
    print("Bem vindo ao jogo da forca!")
    while tentativas != 0:  
        letra = ''
        while len(letra) != 1 and letra not in acertadas and letra not in erradas:
            print_forca(tentativas)
            if len(erradas) != 0:
                print("Já foram erradas as seguintes letras: "+ ', '.join(erradas) + ".")
            print(f"O tema é {tema}.")
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
        if normaliza_simbolos(letra).lower() in normaliza_simbolos(palavra).lower():
            acertadas.append(letra)
            for i in range(len(palavra)):
                if normaliza_simbolos(posicoes[i][0]).lower() == letra:
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