# proxy.py
import socket
import threading

servidores = [('localhost', 6000), ('localhost', 6002), ('localhost', 6004)]  # Endereços dos servidores

def obter_servidor_menos_carregado():
    menorCarga = float('inf')
    melhorServidor = None

    for endereco in servidores:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServidor:
            socketServidor.settimeout(3)  # timeout de 3 segundos para conexão
            try:
                socketServidor.connect((endereco[0], endereco[1]))  # conecta à porta de status
                socketServidor.sendall("STATUS".encode())  # solicita a carga de CPU
                carga = float(socketServidor.recv(1024).decode())  # recebe a carga
                print(f"Servidor {endereco} com carga de CPU: {carga}")
                if carga < menorCarga:
                    menorCarga = carga
                    melhorServidor = endereco
            except (socket.timeout, ConnectionRefusedError, ValueError):
                print(f"Servidor {endereco} indisponível ou com carga desconhecida")
                continue

    return melhorServidor

def atender_cliente(conexaoCliente, enderecoCliente):
    print(f"Conexão recebida de {enderecoCliente}")
    operacao = conexaoCliente.recv(1024).decode()
    
    servidor = obter_servidor_menos_carregado()
    if servidor:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServidor:
            socketServidor.connect((servidor[0], servidor[1] + 1))  # Conecta à porta de serviço
            socketServidor.sendall(operacao.encode())
            resultado = socketServidor.recv(1024).decode()
            conexaoCliente.sendall(resultado.encode())
    else:
        conexaoCliente.sendall("Erro: Nenhum servidor disponível.".encode('utf-8'))
    
    conexaoCliente.close()

def executar_proxy():
    host = '0.0.0.0'
    porta = 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketProxy:
        socketProxy.bind((host, porta))
        socketProxy.listen()
        print("Proxy reverso aguardando conexões de clientes...")

        while True:
            try:
                conexaoCliente, enderecoCliente = socketProxy.accept()
                threading.Thread(target=atender_cliente, args=(conexaoCliente, enderecoCliente)).start()
            except KeyboardInterrupt:
                print("Encerrando proxy reverso...")
                break

if __name__ == "__main__":
    executar_proxy()
