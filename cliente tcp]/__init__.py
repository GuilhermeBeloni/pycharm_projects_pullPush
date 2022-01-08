import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print('A conexão falhou!!!')
        print(f'ERRO: {erro}')
        sys.exit()
    print('Socket criado com sucesso!')

    hostAlvo = input('Digite o Host ou IP a ser conectado: ')
    portaAlvo = input('Digite a Porta a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print(f'Conexão TCP conectada com sucesso no Host {hostAlvo} e Porta {portaAlvo} !!!')
        s.shutdown(2)
    except socket.error as erro:
        print(f'A conexão do Host {hostAlvo} e Porta {portaAlvo} falhou!!!')
        print(f'Erro: {erro}')
        sys.exit()

if __name__ == '__main__':
    main()