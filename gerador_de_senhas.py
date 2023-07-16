import random
import string
import os
from time import sleep

#Seleciona letras, números e pontuações válidas para senha
opcao_letras = string.ascii_letters
opcao_numeros = string.digits
opcao_pontuacoes = string.punctuation
opcoes = opcao_letras + opcao_numeros + opcao_pontuacoes

#Gera uma senha aleatória baseado nos caracteres selecionados e no tamanho escolhido pelo usuário.
def gerador_de_senha(tamanho = 8):

    senha = ''

    for _ in range(0, tamanho):
        digito = random.choice(opcoes)
        senha += digito

    return senha

#Pergunta ao usuário a quantidade de dígitos
while True:

    escolha_do_usuario = input("Quantos digítos na senha?: ")   

    if escolha_do_usuario.isdigit():
        escolha_do_usuario = int(escolha_do_usuario)
        break
    else:
        print("Digite uma quantidade válida! ")
        os.system('cls')
        sleep(1.8)


senha_gerada = gerador_de_senha(tamanho = escolha_do_usuario)

print(senha_gerada)

