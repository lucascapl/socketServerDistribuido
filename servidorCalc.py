# servidor_calculo.py
import socket
import threading
import psutil
import sys

def servidor_status(portaStatus):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketStatus:
        socketStatus.bind(('localhost', portaStatus))
        socketStatus.listen()
        print(f"Servidor de Status rodando na porta {portaStatus}...")

        while True:
            conexaoStatus, _ = socketStatus.accept()
            with conexaoStatus:
                mensagem = conexaoStatus.recv(1024).decode()
                if mensagem == 'STATUS':
                    carga = psutil.cpu_percent(interval=1)
                    conexaoStatus.sendall(str(carga).encode())
                else:
                    conexaoStatus.sendall(b"Erro: Comando desconhecido.")

def calcular_operacao(operacao):
    try:
        partes = operacao.split()
        if len(partes) != 3:
            return "Erro: Formato inválido"
        
        operador1, operador, operador2 = partes
        operador1, operador2 = float(operador1), float(operador2)

        if operador == '+':
            return str(operador1 + operador2)
        elif operador == '-':
            return str(operador1 - operador2)
        elif operador == '*':
            return str(operador1 * operador2)
        elif operador == '/':
            return str(operador1 / operador2) if operador2 != 0 else "Erro: Divisão por zero"
        else:
            return "Erro: Operador desconhecido"
    except ValueError:
        return "Erro: Operandos inválidos"

def servidor_calculadora(portaCalculadora):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCalculadora:
        socketCalculadora.bind(('localhost', portaCalculadora))
        socketCalculadora.listen()
        print(f"Servidor de Cálculo rodando na porta {portaCalculadora}...")

        while True:
            conexaoCalculadora, _ = socketCalculadora.accept()
            with conexaoCalculadora:
                operacao = conexaoCalculadora.recv(1024).decode()
                print(f"Processando operação: {operacao}")
                
                resultado = calcular_operacao(operacao)
                conexaoCalculadora.sendall(resultado.encode())

def executar_servidor(portaStatus, portaCalculadora):
    threading.Thread(target=servidor_status, args=(portaStatus,)).start()
    threading.Thread(target=servidor_calculadora, args=(portaCalculadora,)).start()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python servidor_calculo.py <portaStatus> <portaCalculadora>")
        sys.exit(1)
    
    portaStatus = int(sys.argv[1])
    portaCalculadora = int(sys.argv[2])
    executar_servidor(portaStatus, portaCalculadora)
