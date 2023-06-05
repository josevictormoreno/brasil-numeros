import os
# Limpa a tela do terminal
def clear():
    if os.name == 'posix':  # Para sistemas baseados em Unix (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':  # Para Windows
        os.system('cls')
