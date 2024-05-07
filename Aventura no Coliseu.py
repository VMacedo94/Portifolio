import random

def personagem_dano(ataque_personagem, velocidade_personagem, nivel_personagem):
    return (ataque_personagem + (1 / 2) * velocidade_personagem) * nivel_personagem

def inimigo_dano(ataque_inimigo, nivel_inimigo):
    return ataque_inimigo + nivel_inimigo

def personagem_defesa(defesa_personagem, velocidade_personagem):
    return defesa_personagem + velocidade_personagem

def inimigo_defesa(defesa_inimigo):
    return defesa_inimigo

personagem_vida = 100
nivel_personagem = 1
ataque_personagem = 5
velocidade_personagem = 5  
defesa_personagem = 5

inimigo_vida = 20
nivel_inimigo = 1
ataque_inimigo = 3
defesa_inimigo = 3
velocidade_inimigo = 3

print("Você está caminhando pelo coliseu...") 
print("Entrando na fase de batalha...")
print("Seu inimigo se aproxima e olha atentamente para você...")
print("O que você faz:")

while nivel_personagem < 6:
    inimigo_vida = 20 + random.randint(1,100)
    print("Nível do personagem:", nivel_personagem)
    print(f"Você está enfrentando um inimigo com {inimigo_vida} de vida!")
    while inimigo_vida > 0:
        acao = input("1 - Atacar\n2 - Fugir\n")
        if acao == "1":
            print("Você decidiu enfrentar o perigo!")
            inimigo_vida -= personagem_dano(ataque_personagem, velocidade_personagem, nivel_personagem)
            personagem_vida -= inimigo_dano(ataque_inimigo, nivel_inimigo)
            print(f"Você atacou o inimigo, ele ficou com {inimigo_vida} de vida")
            print(f"O inimigo atacou, você ficou com {personagem_vida} de vida")
            if inimigo_vida <= 0:
                print("Você derrotou o inimigo!")
                print("Você ganhou", nivel_inimigo, "de experiência")
                nivel_personagem += 1
                print("Você subiu de nível, seu nível atual é", nivel_personagem)
                print("Você deseja receber os espólios da sua vitória?")
                receber_espolio = input("1 - Sim\n2 - Não\n")
                if receber_espolio == "1":
                    espolio = random.randint(1, 3)
                    if espolio == 1:
                        print("Você recebeu uma nova espada!")
                        ataque_personagem += 1
                        print("Seu ataque agora é", ataque_personagem)
                    elif espolio == 2:
                        print("Você recebeu um novo escudo!")
                        defesa_personagem += 1
                        print("Sua defesa agora é", defesa_personagem)
                else:
                    print("Você recebeu um toque de cura!")
                    personagem_vida += 10
                    print("Sua vida agora é", personagem_vida)
            else:
                print("O inimigo ainda está de pé!")
        elif acao == "2":
            print("Você está no coliseu, não pode fugir!")
        else:
            print("Comando inválido")
print("Parabéns! Você alcançou o nível 6 e completou sua jornada no coliseu!")
