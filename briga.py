import random
import time

class Duelante:
    def __init__(self, nome, vida, forca, agilidade):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.agilidade = agilidade

    def __str__(self):
        return f"{self.nome} (Vida: {self.vida})"

def rolar_dados(tipo):
    if tipo == "d20":
        return random.randint(1, 20)
    elif tipo == "d12":
        return random.randint(1, 12)
    elif tipo == "d6":
        return random.randint(1, 6)

def calcular_dano(atacante, defensor):
    dano = atacante.forca - defensor.agilidade
    if dano < 5:
        dano = 5
    return dano

def atacar(atacante, defensor):
    rolagem = rolar_dados("d20")
    if rolagem >= 15:
        dano = calcular_dano(atacante, defensor)
        defensor.vida -= dano
        print(f"{atacante.nome} acertou {defensor.nome} e causou {dano} de dano!")
    else:
        print(f"{atacante.nome} errou o ataque!")

def defender(defensor):
    rolagem = rolar_dados("d20")
    if rolagem >= 10:
        print(f"{defensor.nome} defendeu com sucesso!")
    else:
        print(f"{defensor.nome} falhou na defesa!")

def realizar_acao(jogador, adversario):
    print("Escolha uma ação:")
    print("1. Atacar")
    print("2. Defender")
    print("3. Fugir")
    escolha = input("Digite o número da ação: ")
    if escolha == "1":
        atacar(jogador, adversario)
    elif escolha == "2":
        defender(jogador)
    elif escolha == "3":
        print("Você fugiu da luta!")
        return False
    return True

def imprimir_estado_da_luta(jogador, adversario):
    print(f"\n{jogador}")
    print(f"{adversario}")

def realizar_luta(jogador, adversario):
    while True:
        imprimir_estado_da_luta(jogador, adversario)
        if not realizar_acao(jogador, adversario):
            break
        if adversario.vida <= 0:
            print("Você venceu a luta!")
            break
        elif jogador.vida <= 0:
            print("Você perdeu a luta!")
            break
        time.sleep(1)

nome_jogador = input("Digite o seu nome: ")
nome_adversario = "Cavaleiro Negro"

jogador = Duelante(nome_jogador, 100, 10, 10)
adversario = Duelante(nome_adversario, 100, 10, 10)

realizar_luta(jogador, adversario)