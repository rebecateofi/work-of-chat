import socket
import os

# Criação do objeto de socket para o cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão com o servidor
cliente.connect(('localhost', 8888))

# Variável para indicar se o chat foi encerrado
terminado = False

# Mensagens de instrução exibidas ao usuário
print('Digite tt para encerrar o chat')
print('Digite /send_file para enviar arquivo no chat')

# Loop principal do chat
while not terminado:
    # Envio da mensagem digitada pelo usuário para o servidor
    cliente.send(input('Mensagem: ').encode('utf-8'))

    # Recebimento da resposta do servidor
    msg = cliente.recv(1024).decode('utf-8')

    # Verificação se a mensagem recebida indica o envio de arquivo
    if msg.startswith('/send_file'):
        # Extração do nome do arquivo da mensagem recebida
        filename = msg.split()[1]

        # Abertura do arquivo para escrita em modo binário
        with open(filename, 'wb') as f:
            # Loop para receber os dados do arquivo em blocos de 1024 bytes
            while True:
                data = cliente.recv(1024)
                if not data:
                    break
                f.write(data)

            f.close()

        # Impressão de uma mensagem informando o sucesso do recebimento do arquivo
        print('Arquivo recebido com sucesso: ' + filename)

    # Verificação se a mensagem recebida indica o encerramento do chat
    elif msg == 'tt':
        terminado = True
    else:
        # Exibição da mensagem recebida do servidor
        print(msg)

# Fechamento da conexão com o servidor
cliente.close()
