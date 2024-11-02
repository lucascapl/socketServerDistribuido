# cliente.py
import socket

def executar_cliente():
    host = 'localhost'
    porta = 5000  # porta para conexão com o proxy

    while True:
        operacao = input("Digite a operação (exemplo: 3 + 4) ou 'sair' para fechar: ")
        if operacao.lower() == 'sair':
            print("Encerrando cliente.")
            break

        # conecta ao proxy para cada operação
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:
            socketCliente.connect((host, porta))
            socketCliente.sendall(operacao.encode())  # Envia a operação ao proxy
            resultado = socketCliente.recv(1024).decode()  # Recebe e exibe o resultado
            print("Resultado:", resultado)

if __name__ == "__main__":
    executar_cliente()
