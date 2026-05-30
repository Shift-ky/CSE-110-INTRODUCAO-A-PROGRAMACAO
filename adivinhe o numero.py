





# Importação do método random, para setar uma numeração aleatória.
import random

# variáveis de instruções e de validações
jogando        = True
numero_acertado = None
tentativas     = 0
numero_maquina = random.randint(1,10)
mensagem = 'Olá eu já escoli o meu número, Agora...'

#Laço de repetição para jogar quantaas veses quuiser
while jogando:
    # Toda vez que o jogador reiniciar a partida, as variáveis serão limpas, e um novo número será setado.
    numero_acertado = None
    tentativas     = 0
    numero_maquina = random.randint(1,10)
    
    print("\033c", end="") # Código para limpar a tela
    print(mensagem)

    while numero_acertado is None:
        
        tentativas += 1 
        palpite = int(input('Qual é o seu paupite? '))
    
        if palpite < numero_maquina:
            print('Mais alto')
        elif palpite > numero_maquina:
            print('Mais baixo')
        else:
            print('Você acertou!')
            numero_acertado = True
            print(f'Você precisou de {tentativas} tentativas')
    
    jogando = input('Continuar ? [S]im ou [N]ão: ').upper().startswith('S') # Validação do jogador, para saber se quer continuar jogando, a entrada está tratada para pegar a primeira letra do que digitar, independente se colocar só S ou SIM
print('Até a próxima :)')