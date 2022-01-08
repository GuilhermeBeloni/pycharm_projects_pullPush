from time import sleep
from Menu.Menu01 import *

estoque = []


def cNECria():
    try:
        arq = open('controle_estoque.txt', 'r')
        arq.close()
    except FileNotFoundError:
        print('O Arquivo não existente...')
        sleep(1)
        print('Criando arquivo...')
        sleep(1)
        arq = open('controle_estoque.txt', 'wt+')
        print(f'Arquivo criado com sucesso!')
        arq.close()


def grava_txt():
    with open('controle_estoque.txt', 'wt+') as arquivo:
        for elemento in estoque:
            arquivo.write(f'{elemento[0]};{elemento[1]};{elemento[2]};{elemento[3]}\n')




def cadastro():
    retorno = 'S'
    while retorno == 'S':
        cabecalho('Cadastro')
        produto = input('Nome do produto: ').upper()
        estoque.append([produto, lerInt('Quantidade: '), lerFloat('Valor de compra: '), lerFloat('Valor de venda: ')])
        grava_txt()
        print(f'{produto} cadastrado(a) com sucesso!')
        retorno = input('Deseja continuar cadastrando? <S/N>').upper()




def exibe_estoque():
    cabecalho('Estoque')
    print('Prod           Quant  PC      PV')
    print('--' * 20)
    with open('controle_estoque.txt', 'r') as arquivo:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<15}Un{dado[1]:<5}R${dado[2]:<6}R${dado[3]:>3}')



'''def reg_compra():
    retorno = 'S'
    while retorno == 'S':'''



