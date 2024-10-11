import random

def Exercicio5():
    
    opcoes = ["Pedra", "Papel", "Tesoura"]
    jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
    maquina = random.choice(opcoes)
    
    print(f"Jogador escolheu: {jogador}")
    print(f"Máquina escolheu: {maquina}")
    
    if jogador == maquina:
        
        print("Jogo empatou")
        
    elif (jogador == "Pedra" and maquina == "Tesoura") or \
         (jogador == "Papel" and maquina == "Pedra") or \
         (jogador == "Tesoura" and maquina == "Papel"):
             
        print("Você venceu!")
        
    else:
        print("Você perdeu!")

Exercicio5()
