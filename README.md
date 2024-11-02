
# Calculadora Distribuída com Balanceamento de Carga

Este projeto é uma aplicação distribuída implementada em Python utilizando sockets, composta por um cliente, um proxy reverso e múltiplos servidores de cálculo. O objetivo principal é implementar a lógica de balanceamento de carga, onde o proxy reverso seleciona o servidor com menor carga de CPU para processar as requisições do cliente. Este trabalho foi desenvolvido para a disciplina de **Sistemas Distribuídos** na **UERJ**.

## Arquitetura

A aplicação é composta por três componentes principais:
- **Cliente**: Envia operações matemáticas para o proxy reverso e recebe o resultado da operação.
- **Proxy Reverso**: Recebe as requisições dos clientes, seleciona o servidor menos carregado com base na carga de CPU e repassa a requisição ao servidor apropriado.
- **Servidores de Cálculo**: Cada servidor escuta em duas portas (uma para o status de CPU e outra para o serviço de calculadora) e realiza operações matemáticas. A carga de CPU é reportada ao proxy para balanceamento de carga.

## Pré-requisitos

- Python 3.8+
- Biblioteca `psutil` para monitoramento de CPU. Instale usando o comando:
  ```bash
  pip install psutil
  ```

## Estrutura de Arquivos

- `cliente.py`: Implementação do cliente que envia operações ao proxy reverso.
- `proxy.py`: Proxy reverso que distribui as operações aos servidores com menor carga.
- `servidorCalculo.py`: Servidor de cálculo que realiza operações matemáticas e reporta sua carga de CPU.

## Funcionalidades

1. **Cliente**:
   - Conecta-se ao proxy reverso e envia uma requisição com a operação matemática.
   - Recebe e exibe o resultado da operação.

2. **Proxy Reverso**:
   - Escuta na porta 5000 para receber requisições dos clientes.
   - Seleciona o servidor menos carregado (menor uso de CPU) para encaminhar a requisição.
   - Redireciona a resposta do servidor para o cliente.

3. **Servidor de Cálculo**:
   - Escuta na porta de status e responde ao proxy com a carga de CPU.
   - Escuta na porta de serviço para receber operações matemáticas e processar o cálculo.
   - Exibe o resultado da operação no console para depuração.

## Executando o Projeto

1. Inicie os servidores:
   - Em 3 terminais diferentes, execute `servidorCalculo.py` especificando as portas de status e serviço. Exemplo:
     ```bash
     python servidorCalculo.py 6000 6001
     python servidorCalculo.py 6002 6003
     python servidorCalculo.py 6004 6005
     ```

2. Inicie o proxy reverso:
   - Em outro terminal, execute:
     ```bash
     python proxy.py
     ```

3. Inicie o cliente:
   - Em um outro terminal, execute:
     ```bash
     python cliente.py
     ```
   - Ao final, deve haver 5 consoles abertos, 3 com servidoresCalc, 1 com proxy e 1 com o cliente
   - Insira uma operação matemática (exemplo: `3 + 4`) e observe o resultado.

## Exemplo de Operação

Ao executar o cliente e inserir a operação `3 + 4`, o fluxo é o seguinte:
1. O cliente envia a operação ao proxy.
2. O proxy consulta a carga de CPU dos servidores e seleciona o menos carregado.
3. O proxy envia a operação ao servidor escolhido.
4. O servidor processa a operação e envia o resultado ao proxy.
5. O proxy retorna o resultado ao cliente.

## Notas Importantes

- **Timeout no Proxy**: O proxy possui um timeout para conexões com servidores, o que evita bloqueios se um servidor estiver indisponível.
- **Segurança nas Operações**: A função de cálculo no servidor foi implementada para permitir apenas operações básicas (soma, subtração, multiplicação e divisão), garantindo segurança contra execução de código arbitrário.
- 
## Licença

Este projeto foi desenvolvido como parte de um trabalho acadêmico para a disciplina de Sistemas Distribuídos na UERJ.
