@echo off
start cmd /k "python proxy.py"

start cmd /k "python servidorCalc.py 6000 6001"

start cmd /k "python servidorCalc.py 6002 6003"

start cmd /k "python servidorCalc.py 6004 6005"

start cmd /k "python cliente.py"