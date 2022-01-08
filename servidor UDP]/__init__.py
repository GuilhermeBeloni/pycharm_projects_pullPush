import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!')

host = 'localhost'
porta = 5432

s.bind((host, porta))
msg = '\nServidor: Eaew Cliente? BÃO e vc?'
while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (msg.encode()), endereco)