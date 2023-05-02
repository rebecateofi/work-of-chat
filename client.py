import socket
import os
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8888))

terminado = False
print('Digite tt para encerrar o chat')
print('Digite /send_file para enviar arquivo no chat')
while not terminado:
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg.startswith('/send_file'):
        filename = msg.split()[1]
        with open(filename, 'wb') as f:
            while True:
                data = cliente.recv(1024)
                if not data:
                    break
                f.write(data)
            f.close()
        print('Arquivo recebido com sucesso: ' + filename)


    
    elif msg == 'tt':
        terminado = True
    else:
        print(msg)
cliente.close()
