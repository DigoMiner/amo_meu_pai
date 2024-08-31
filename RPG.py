import random

# Defina as características do personagem
nome = input("Digite o nome do seu personagem: ")
classe = input("Escolha a classe do seu personagem (Guerreiro, Mago, Ladino): ")
nivel = 1
vida = 100
forca = 10
agilidade = 10
inteligencia = 10

# Defina as características do monstro
monstro_nome = "Goblin"
monstro_vida = 50
monstro_forca = 5
monstro_agilidade = 5
monstro_inteligencia = 5

# Função para rolar dados
def rolar_dados(tipo):
    if tipo == "d20":
        return random.randint(1, 20)
    elif tipo == "d12":
        return random.randint(1, 12)
    elif tipo == "d6":
        return random.randint(1, 6)

# Função para calcular o dano
def calcular_dano(atacante, defensor):
    dano = atacante["forca"] - defensor["agilidade"]
    if dano < 0:
        dano = 0
    return dano

# Função para realizar um ataque
def atacar(atacante, defensor):
    rolagem = rolar_dados("d20")
    if rolagem >= 15:
        dano = calcular_dano(atacante, defensor)
        defensor["vida"] -= dano
        print(f"{atacante['nome']} acertou {defensor['nome']} e causou {dano} de dano!")
    else:
        print(f"{atacante['nome']} errou o ataque!")

# Função para realizar uma ação
def realizar_acao(personagem):
    print("Escolha uma ação:")
    print("1. Atacar")
    print("2. Defender")
    print("3. Usar habilidade")
    escolha = input("Digite o número da ação: ")
    if escolha == "1":
        atacar(personagem, monstro)
    elif escolha == "2":
        print("Você está defendendo!")
    elif escolha == "3":
        print("Você está usando uma habilidade!")

# Loop do jogo
while True:
    print(f"\n{nome} (Nível {nivel})")
    print(f"Vida: {vida}")
    print(f"Força: {forca}")
    print(f"Agilidade: {agilidade}")
    print(f"Inteligência: {inteligencia}")
    print(f"\n{monstro_nome}")
    print(f"Vida: {monstro_vida}")
    print(f"Força: {monstro_forca}")
    print(f"Agilidade: {monstro_agilidade}")
    print(f"Inteligência: {monstro_inteligencia}")
    realizar_acao({"nome": nome, "vida": vida, "forca": forca, "agilidade": agilidade, "inteligencia": inteligencia})
    if monstro_vida <= 0:
        print("Você derrotou o monstro!")
        break
    elif vida <= 0:
        print("Você foi derrotado!")
        break