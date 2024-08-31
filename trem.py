import os
import time

# Defina a largura da tela
largura_tela = 80

# Defina o trem
trem = """
   _______
  /        \\
 /          \\
|   _____  |
 _| |       |_
  | |       |
  | |_____  |
  |_________|
"""

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para imprimir o trem na tela
def imprimir_trem(posicao):
    limpar_tela()
    print(" " * posicao + trem)

# Simula o trem passando na tela
for posicao in range(largura_tela + len(trem)):
    imprimir_trem(posicao)
    time.sleep(0.1)