
'''
Author Robson Paiva

Atividade sobre criação de histórias para prática de decisões.

O código tem várias tomadas de decições, e cada decição tem o seu rumo da história e o seu final apropriado
'''

# Cabecalho

print('=' * 30)
print(f'{"Olá amante de aventura":^30}')
print('=' * 30)

#Fim do Cabecalho
 

print('Para essa história ainda ficar melhor me diga o seu nome')
nome = input('→ ') # Vareável 

print()
print(f'Prazer em conhece-ló {nome}!,\n Vamos nessa! 😉')
print()
print(f'Você é um jovem caçador chamado {nome}, conhecido por sua coragem nas terras geladas de Northgard. Em uma noite chuvosa, o chefe da vila pede sua ajuda:')
print('— “Uma criatura misteriosa está atacando nossos animais. Vá até a Floresta Sombria e descubra o que está acontecendo.”')
print('Antes de sair, o ferreiro da vila oferece dois itens:')
print('• ARCO\n • TOCHA \n→ Escolha um item.')

item = input('→ ').upper() 

if item == 'ARCO': # Entrada do if se a escolha for ARCO
    print(' Você pega o arco e entra silenciosamente na floresta. O som das folhas secas ecoa enquanto você segue pegadas enormes no chão. Depois de alguns minutos, você vê dois caminhos:')
    
    print(' • Seguir o SOM DO RIO \n• Entrar na CAVERNA ESCURA')
    escolha1 = input('→ ').upper()
    
    if escolha1 == 'SEGUIR O SOM DO RIO' or escolha1 == 'SOM DO RIO' or escolha1 == 'SOM':
        print('Você chega perto de um rio e encontra a criatura bebendo água. Ela parece ferida. O que você faz?')
        print('• ATIRAR \n• OBSERVAR')
        
        escolha2 = input('→ ').upper()
        
        if escolha2 == 'ATIRAR':
            print('Você dispara uma flecha. A criatura ruge furiosamente e corre em sua direção. \nVocê decide:')
            print('• LUTAR \n• CORRER')
            
            escolha3 = input('→ ').upper()
            
            if escolha3 == 'LUTAR':
                print('Após uma batalha intensa, você derrota a criatura e retorna como herói para a vila.')
            elif escolha3 == 'CORRER':
               print('Você tropeça em uma raiz e a criatura alcança você na escuridão.')
                
        elif escolha2 == 'OBSERVAR':
            print('Você percebe que a criatura está presa em uma armadilha de caçadores ilegais.\nVocê decide:')
            print('• AJUDAR a criatura\n• DEIXAR ela presa')
            
            escolha4 = input('→ ').upper()
            
            if escolha4 == 'AJUDAR' or escolha4 == 'AJUDAR A CRIATURA':
                print('A criatura é, na verdade, um lobo gigante raro. Ela foge sem atacar você. Dias depois, a vila percebe que os ataques pararam.')
            elif escolha4 == 'DEIXAR' or escolha4 == 'DEIXAR ELA PRESA':
                print('Outras criaturas aparecem atraídas pelos gritos do animal. Você é cercado.')
            
    elif escolha1 == 'ENTRAR NA CAVERNA ESCURA' or 'CAVERNA ESCURA' or 'CAVERNA':
        print('Dentro da caverna, você encontra ossos espalhados e um brilho dourado no fundo.\nVocê decide:')
        print('• PEGAR O TESOURO\n • INVESTIGAR O BARULHO')
        escolha5 = input('→ ').upper()
        
        if escolha5 == 'PEGAR TESOURO' or escolha5 =='PEGAR':
            print('Ao tocar o ouro, armadilhas antigas são ativadas e pedras começam a cair. \nVocê decide:')
            print('• CORRER PARA A SAÍDA \n• PROTEGER O TESOURO')
            
            escolha6 = input('→ ').upper()
            if escolha6 == 'CORRER PARA A SAÍDA' or escolha6 == 'CORRER' or escolha6 == 'SAIDA':
                print('Você consegue escapar com vida, mas sem nenhum tesouro.')
                
            elif escolha6 == 'PROTEGER O TESOURO' or escolha6 == 'PROTEGER' or escolha6 == 'TESOURO':
                print('A caverna desaba completamente.')
                
        elif escolha5 == 'INVERTIGAR O BARULHO' or escolha5 == 'INVESTIGAR' or  escolha5 == 'BARULHO':
            print('Você encontra um velho caçador ferido. \nEle diz: — “A criatura não é o verdadeiro monstro…”')

            print('Você decide:\n • OUVIR o velho \n• IGNORAR e continuar')
            escolha7 = input('→ ').upper()
            
            if escolha7 == 'OUVIR O VELHO' or escolha7 == 'OUVIR':
                print('O velho revela que bandidos estavam assustando a vila para roubar recursos. Juntos, vocês derrotam os criminosos.')
            elif escolha7 == '' or escolha7 =='':
                print('Você entra mais fundo na caverna e nunca mais é visto.')
            
    
elif item == 'TOCHA':
    print('Você acende a tocha e segue pela floresta iluminando o caminho. O fogo afasta pequenos animais, mas chama atenção de algo grande. \nVocê encontra:')
    print('• UMA CABANA ABANDONADA \n• UMA TRILHA DE SANGUE')
    escolha8 = input('→ ').upper()
    
    if escolha8 == 'UMA CABANA ABANDONADA'or escolha8 == 'CABANA':
        print('Dentro da cabana há um mapa antigo e uma espada enferrujada. \nVocê decide:')
        print('• PEGAR O MAPA \nPEGAR A ESPADA')
        
        escolha9 = input('→ ').upper()
        
        if escolha9 == 'PEGAR O MAPA' or escolha9 =='MAPA':
            print('O mapa mostra um atalho seguro pela floresta. Você encontra a criatura dormindo. \nVocê decide:')
            print('• ATACAR DORMINDO \n• SAIR SEM FAZER BARULHO')
            
            escolha10 = input('→ ').upper()
            if escolha10 == 'ATACAR DORMINDO' or escolha10 == 'ATACAR':
                print('Você derrota a criatura facilmente e salva a vila.')
                
            elif escolha10 == 'SAIR SEM FAZER BARULHO' or escolha10 == 'SAIR':
                print('Você percebe que a criatura estava protegendo filhotes.')
                
        elif escolha9 == 'PEGAR A ESPADA' or escolha9 =='ESPADA':
            print('A espada estava amaldiçoada. Sombras começam a seguir você. \nVocê decide:')
            print('• JOGAR A ESPADA FORA\n• CONTINUAR USANDO')
            
            escolha11 = input('→ ').upper()
            
            if escolha11 == 'JOGAR A ESPADA FORA' or escolha11 == 'JOGAR A ESPADA' or escolha11 == 'JOGAR':
                print('A maldição desaparece e você consegue voltar para casa.')
                
            elif escolha11 == 'CONTINUAR USANDO' or escolha11 == 'CONTINUAR' or escolha11 == 'USANDO':
                print('As sombras consomem sua mente.')
        
    elif escolha8 == 'UMA TRILHA DE SANGUE'or escolha8 == 'TRILHA':
        print('Você segue os rastros até um campo aberto e encontra dois lobos gigantes. \nVocê decide:')
        print('• SUBIR EM UMA ÁRVORE \n• ENFRENTAR OS LOBOS')
        escolha12 = input('→ ').upper()
        
        if escolha12 == 'SUBIR EM UMA ÁRVORE' or escolha12 == 'SUBIR' or escolha12 == 'ÁRVORE':
            print('Você espera até amanhecer e os lobos vão embora.')
        elif escolha12 == 'ENFRENTAR OS LOBOS' or escolha12 == 'ENFRENTAR' or 'LOBOS':
            print('Você luta bravamente, mas os lobos são rápidos demais.')

    