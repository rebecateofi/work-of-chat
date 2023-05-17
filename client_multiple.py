import socket

# Criação do objeto de socket para o cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão com o servidor
cliente.connect(('localhost', 8889))

# Variável para indicar se o chat foi encerrado
terminado = False

# Mensagem exibida ao usuário para encerrar o chat
print('Digite tt para encerrar o chat')

# Loop principal do chat
while not terminado:
    # Recebimento da mensagem digitada pelo usuário
    mensagem = input('Mensagem: ')

    # Verificação se a mensagem indica o encerramento do chat
    if mensagem == 'tt':
        # Envio da mensagem ao servidor e interrupção do loop
        cliente.send(mensagem.encode('utf-8'))
        break

    # Envio da mensagem ao servidor
    cliente.send(mensagem.encode('utf-8'))

    # Recebimento da resposta do servidor
    resposta = cliente.recv(1024).decode('utf-8')

    # Exibição da resposta do servidor
    print(resposta)

# Fechamento da conexão com o servidor
cliente.close()
