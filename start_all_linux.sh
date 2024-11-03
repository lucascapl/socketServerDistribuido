#!/bin/bash
# Script para iniciar o proxy, servidores e cliente em novas janelas de terminal no Linux

# Inicia o proxy em uma nova janela de terminal
gnome-terminal -- bash -c "python3 proxy.py; exec bash"

# Inicia o primeiro servidor de cálculo (Status na porta 6000, Serviço na porta 6001)
gnome-terminal -- bash -c "python3 servidorCalc.py 6000 6001; exec bash"

# Inicia o segundo servidor de cálculo (Status na porta 6002, Serviço na porta 6003)
gnome-terminal -- bash -c "python3 servidorCalc.py 6002 6003; exec bash"

# Inicia o terceiro servidor de cálculo (Status na porta 6004, Serviço na porta 6005)
gnome-terminal -- bash -c "python3 servidorCalc.py 6004 6005; exec bash"

# Inicia o cliente em uma nova janela de terminal
gnome-terminal -- bash -c "python3 cliente.py; exec bash"
