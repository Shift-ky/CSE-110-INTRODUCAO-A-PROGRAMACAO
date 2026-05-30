from random import sample
from random import choice

'''
Código criado por Robson dia 30/05/2026

Para a melhoria do código foram adicionados os seguintes melhorias

1º Uma lista para pegar os nomes aleatórios
2º Laço de repetição caso queira jogar mais de uma vez
'''

# Declaração de dados
nomes = [
    'Moisés',
    'Abraão',
    'Isaque',
    'Jacó',
    'José',
    'Noé',
    'Davi',
    'Salomão',
    'Samuel',
    'Elias',
    'Isaías',
    'Jeremias',
    'Daniel',
    'Ester',
    'Rute',
    'Maria',
    'Pedro',
    'João',
    'Paulo',
    'Néfi',
    'Leí',
    'Saria',
    'Enos',
    'Mosias',
    'Benjamim',
    'Alma',
    'Helamã',
    'Morôni'
]


palavra_secreta = ''
palavra_digitada = ''
validador_palavra = ''
palavra = ''
tentativas = 0 
jogando = True

## Fim da declaração de dados

while jogando:
    palavra_secreta = choice(nomes)
    palavra = ''
    tentativas = 0
    print("\033c", end="") # Código para limpar a tela
    
    print(f"Sua dica é: {'_' * len(palavra_secreta)}")

    while True:
        print(palavra_secreta)
        validador_palavra = ''
        palavra_digitada =  input('Qual é o seu palpite: ')

        validador_palavra += palavra_digitada
        tentativas += 1
        
        if len(palavra_secreta) != len(palavra_digitada):
            print('Desculpe, o palpite precisa ter o mesmo número de letras que a palavra secreta.')
            print(f"Sua dica é: {palavra}")
            continue
            
        if palavra_secreta == palavra_digitada:
            print(f'Parabéns você acertou a palavra após {tentativas} tentativas')
            break       
        # Validação para ser digitado apenas letras
        palavra = ''
        validador_palavra = ''.join(sample(palavra_digitada, len(palavra_digitada)))
        for i, letra in enumerate(validador_palavra):
            if letra in palavra_secreta:
                if i < len(validador_palavra) and palavra_secreta[i] == letra:
                    palavra += letra.upper()  # posição correta
                else:
                    palavra += letra.lower()  # letra existe mas está em outra posição
            else:
                palavra += "_" # Letras que ainda não foram descoberta

        print(f"Sua dica é: {palavra}")
    jogando = input('Continuar? [S]im ou [N]ão: ').upper().startswith('S')
print('Até logo!')