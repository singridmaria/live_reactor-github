# Importar o módulo randow

import random

options = ["pedra","papel","tesoura"] # creating a list of options
score = 0
rounds_played = 0

while True:
    random_choice = random.choice(options) # random choice from the list
    player_choice = input("Escolha pedra, papel ou tesoura: ") # player choice

    # Se o meu jogador escolher pedra

    if player_choice == "pedra":
        rounds_played +=1
        if random_choice == "pedra":
            print("Empate!")
        elif random_choice == "papel":
            print("Você perdeu!")
        elif random_choice == "tesoura":
            print("Você ganhou!")
            score += 1 
    

    # Se o meu jogador escolher papel

    if player_choice == "papel":
        rounds_played +=1
        if random_choice == "pedra":
            print("Você ganhou!")
        elif random_choice == "papel":
            print("Empate!")
        elif random_choice == "tesoura":
            print("Você perdeu!")
            score += 1 



    # Se o meu jogador escolher tesoura

    if player_choice == "tesoura":
        rounds_played +=1
        if random_choice == "pedra":
            print("Você perdeu!")
        elif random_choice == "papel":
            print("Você ganhou!")
        elif random_choice == "tesoura":
            print("Empate!")
            score += 1 
    

    # Seo o meu jogador escolher algo diferente de pedra, papel ou tesoura

    else:
        play_again = input("Deseja jogar novamente? (s/n) ")
        if play_again == "s":
            continue

        elif play_again == "n":
            print("Você ganhou: ", score, "Vezes!", rounds_played, " rodadas jogadas!" )
            break


        print("Escolha inválida!")
        

    

    



