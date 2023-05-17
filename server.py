import socket
import os

# Criação do objeto de socket para o servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculação do servidor ao endereço e porta
servidor.bind(('localhost', 8888))

# Início da escuta por conexões
servidor.listen()

# Aceitação de uma conexão do cliente
cliente, end = servidor.accept()

# Variável para indicar se o chat foi encerrado
terminado = False

# Loop principal do chat
while not terminado:
    # Recebimento da mensagem do cliente
    msg = cliente.recv(1024).decode('utf-8')

    # Verificação se a mensagem indica o envio de arquivo
    if msg.startswith('/send_file'):
        # Extração do nome do arquivo da mensagem recebida
        filename = msg.split()[1]

        # Verificação se o arquivo existe
        if os.path.exists(filename):
            # Abertura do arquivo para leitura em modo binário
            with open(filename, 'rb') as f:
                # Envio da mensagem original ao cliente
                cliente.send(msg.encode('utf-8'))

                # Leitura e envio dos dados do arquivo em blocos de 1024 bytes
                data = f.read(1024)
                while data:
                    cliente.send(data)
                    data = f.read(1024)
                f.close()

            print('Arquivo enviado com sucesso: ' + filename)
        else:
            print('Arquivo não encontrado: ' + filename)
    else:
        # Verificação se a mensagem indica o encerramento do chat
        if msg == 'tt':
            terminado = True
        else:
            # Exibição da mensagem recebida do cliente
            print(msg)

    # Envio da mensagem digitada pelo usuário para o cliente
    cliente.send(input('Mensagem: ').encode('utf-8'))

# Fechamento da conexão com o cliente
cliente.close()

# Fechamento do socket do servidor
servidor.close()
