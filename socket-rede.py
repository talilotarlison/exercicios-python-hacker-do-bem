import socket

# Cria um objeto socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket a um endereço e porta
server_address = ('localhost', 10000)
print(f'Conectando a {server_address[0]} na porta {server_address[1]}')
sock.connect(server_address)

try:
    # Envia dados
    message = 'Olá, mundo!'
    print(f'Enviando "{message}"')
    sock.sendall(message.encode())

    # Procura a resposta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'Recebido "{data.decode()}"')

finally:
    print('Fechando o socket')
    sock.close()
