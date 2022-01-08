from Menu.defsarquivo import *

cNECria()

while True:
    resp = menu(['CADASTRAR UM PRODUTO', 'REGISTRO DE COMPRA', 'REGISTRO DE VENDA',
                 'ALTERAR UM PRODUTO', 'EXCLUIR UM PRODUTO', 'CONSULTAR ESTOQUE',
                 'CONSULTAR LUCRO\n', 'SAIR DO SISTEMA'])

    if resp == 1:
        cadastro()

    #elif resp == 2:
        #reg_compra()


    elif resp == 6:
        exibe_estoque()

    elif resp == 8:
        print('Programa encerrado...')
        sleep(2)
        cabecalho('Até logo!')
        break





