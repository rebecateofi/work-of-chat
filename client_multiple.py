import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8889))

terminado = False
print('Digite tt para encerrar o chat')
while not terminado:
    mensagem = input('Mensagem: ')
    if mensagem == 'tt':
        cliente.send(mensagem.encode('utf-8'))
        break
    cliente.send(mensagem.encode('utf-8'))
    resposta = cliente.recv(1024).decode('utf-8')
    print(resposta)
cliente.close()