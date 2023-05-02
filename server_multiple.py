import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8889))

servidor.listen()
clientes = []

terminado = False

while not terminado:

    cliente, end = servidor.accept()
    clientes.append(cliente)  # Adiciona o novo cliente na lista
    print(f'Nova conexão de {end}')
    while True:
        try:
            msg = cliente.recv(1024).decode('utf-8')
            if msg:
                print(f'Mensagem recebida de {end}: {msg}')
                # Envia a mensagem para todos os clientes, exceto o remetente
                for c in clientes:
                    if c != cliente:
                        c.send(msg.encode('utf-8'))
                cliente.send('Mensagem recebida'.encode('utf-8'))  # Confirmação de leitura para o remetente
            else:
                print(f'{end} desconectou')
                clientes.remove(cliente)  # Remove o cliente da lista
                cliente.close()
                break
        except:
            print(f'Erro de conexão com {end}')
            clientes.remove(cliente)  # Remove o cliente da lista
            cliente.close()
            break
cliente.close()
servidor.close()
