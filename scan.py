import socket
import time

#IP do host inputado pelo usuario
host = input("Digite o endereço IP do host: ")
min_port = int(input("Digite o número da porta mínima a ser verificada: "))
max_port = int(input("Digite o número da porta máxima a ser verificada: "))

print(f"Iniciando scan de portas para o host: {host}")

#Range de portas
for port in range(min_port, max_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Porta {port} aberta")
    sock.close()
