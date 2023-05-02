import socket
import os
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

servidor.listen()
cliente, end = servidor.accept()
terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg.startswith('/send_file'):
        filename = msg.split()[1]
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                cliente.send(msg.encode('utf-8'))
                data = f.read(1024)
                while data:
                    cliente.send(data)
                    data = f.read(1024)
                f.close()
            print('Arquivo enviado com sucesso: ' + filename)
        else:
            print('Arquivo não encontrado: ' + filename)
    else:
        if msg == 'tt':
            terminado = True
        else:
            print(msg)
    cliente.send(input('Mensagem: ').encode('utf-8'))
cliente.close()
servidor.close()
