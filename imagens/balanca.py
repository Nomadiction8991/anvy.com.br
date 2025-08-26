""" Simulador de balança em rede

Utilize para testar comunicação com balanças.
"""
import sys
import socket
import itertools

pesos = [388, 150, 445, 223, 589, 1250] # Valores aleatórios
iterador_pesos = itertools.cycle(pesos)

HOST = '127.0.0.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

def aguarda_conexao():
    while True:
        conn, addr = s.accept()
        print('Nova conexão de', addr)

        while True:
            try:
                data = conn.recv(1024)
            except socket.error:
                conn.close()
                break

            if not data:
                break
            
            print('recv:', data)

            peso_aleatorio = '{0}'.format(next(iterador_pesos)).encode('latin1')
        
            print('send:', peso_aleatorio)
            conn.send(peso_aleatorio)

        conn.close()
        print('Conexão finalizada.')
        sys.exit(0)

print('Simulador de balança iniciado na porta {}'.format(PORT))

while True:
    try:
        aguarda_conexao()
    except socket.error as e:
        print(e)
        continue
