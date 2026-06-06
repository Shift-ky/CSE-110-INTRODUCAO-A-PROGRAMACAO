import time

# Author Robson Paiva
# Data criação 06/06/2026
# Para a parte criativa adicionei a quantidade de itens que o cliente quer levar
# Crie um layout para que o cliente possa ver os produtos em forma de cupom
# Foi adicionado um Timer para que possa dar um tempo antes de limpar a tela e recomeçar o processo
# Foi adicionado uma nova opção para alterar a quantidade e valor do produto


soma_produto = 0
carrinho_compra_produto    = []
carrinho_compra_preco      = []
carrinho_compra_quantidade = []
produto = ''
valor = 0
quantidade = 0
produto_selecionado = 0

print('Bem-vindos ao Programa de Carrinho de Compras!')

while True:
    
    print('''
Selecione uma das seguintes ações:
1. Adicionar item
2. Ver carrinho
3. Remover item
4. Calcular o total
5. Alterar Produto
6. Sair    
''')
    opcao = input('Por favor, insira uma ação: ')
    
   
    
    if opcao == '1': #Adicionar produtos
        try:
            
            produto    = input('Qual produto quer adicionar: ')
            valor      = float(input('Valor do produto: ').replace(',','.')) # Tratativa para adicionar tanto com ponto quanto com virgula
            quantidade = int(input('Quantidade: ')) # Caso for digitado um espaço, será trocado por um valor numérico
            
            carrinho_compra_produto.append(produto)
            carrinho_compra_preco.append(int(valor))
            carrinho_compra_quantidade.append(int(quantidade))
            
            print(f'Produto: {produto}\nQuantidade: {quantidade}\nvalor: {valor:.2f}\nadicionado com sucesso.')
            time.sleep(2)
            print("\033c", end="")
            
        except:
            print('Infome um valor válido.')
            print('Você será redirecionado ao início')
            time.sleep(2)
            print("\033c", end="")
        
       
        
      
      
    elif opcao == '2': # Ver os produtos do carrinho
        
        print("\033c", end="") #Linmpa a tela
        print(f"{'ITEM':<6} {'PRODUTO':<16} {'QTD':<3} {'VALOR':>16}")
        print("-" * 50) 
        
        if len(carrinho_compra_produto) > 0: # Validação para não dar erro de possição 
            
          for i in range(len(carrinho_compra_produto)):
               
            print(f' {i + 1:.<6} {carrinho_compra_produto[i]:.<17}{carrinho_compra_quantidade[i]:.<14}R$ {carrinho_compra_preco[i]:4.2f}')
            print("-" * 50)
                
        else:
            
            print('Carrinho de compras está vazio.')
            print('Você será redirecionado ao início')
            time.sleep(2)
            print("\033c", end="")
                    
    elif opcao == '3': # Remover produtos do carrinho
        
        if len(carrinho_compra_produto) > 0: # Validação para não dar erro de possição 
            print("\033c", end="") #Linmpa a tela
            print(f"{'ITEM':<6} {'PRODUTO':<16} {'QTD':<3} {'VALOR':>16}")
            print("-" * 50) 
            
            for i in range(len(carrinho_compra_produto)): # Rotina para listar os produtos do carrinho   
                print(f' {i + 1:.<6} {carrinho_compra_produto[i]:.<17}{carrinho_compra_quantidade[i]:.<14}R$ {carrinho_compra_preco[i]:4.2f}')
                print("-" * 50)
            try:    
                produto_deletado = int(input('Informe o produto que queira remover: '))
                produto_deletado -=1
                if produto_deletado ==-1:
                    print('Desculpe, esse número de item não é válido.')
                    print('Você será redirecionado ao início')
                
                    time.sleep(2)
                    print("\033c", end="")
                    continue
            except ValueError:
                print('Informe um valor válido')
            if int(produto_deletado) >= len(carrinho_compra_produto):
                
                print('Desculpe, esse número de item não é válido.')
                print('Você será redirecionado ao início')
                
                time.sleep(2)
                print("\033c", end="")
                continue
            
            carrinho_compra_produto.pop(int(produto_deletado))
            carrinho_compra_preco.pop(int(produto_deletado))
            carrinho_compra_quantidade.pop(int(produto_deletado))
            print('Item removido.')
            
        else:
            
            print('Carrinho de compras está vazio.')
            print('Você será redirecionado ao início')
            time.sleep(2)
            print("\033c", end="")
        
    elif opcao == '4':
        
        if len(carrinho_compra_preco) > 0: # Validar a quantidade de itens no carrinho
            soma_produto = 0 # Zerar a variável
            
            for i in range(len(carrinho_compra_preco)): # fazer o calculo dos produtos
                soma_produto +=  carrinho_compra_preco[i] * carrinho_compra_quantidade[i]
                
            print(f'O preço total dos itens no carrinho de compras é de R$ {soma_produto:4.2f}')
        else:
            print('Carrinho de compras está vazio.') 
            print('Você será redirecionado ao início')
            time.sleep(2)
            print("\033c", end="")
        
    elif opcao == '5':
        if len(carrinho_compra_produto) > 0: # Validação para não dar erro de possição 
            print("\033c", end="") #Linmpa a tela
            print(f"{'ITEM':<6} {'PRODUTO':<16} {'QTD':<3} {'VALOR':>16}")
            print("-" * 50) 
            for i in range(len(carrinho_compra_produto)): # Rotina para listar os produtos do carrinho
                
                print(f' {i + 1:.<6} {carrinho_compra_produto[i]:.<17}{carrinho_compra_quantidade[i]:.<14}R$ {carrinho_compra_preco[i]:4.2f}')
                print("-" * 50)
            try:    
                produto_selecionado = int(input('Informe o produto que queira alterar: '))
                produto_selecionado -=1
                if produto_deletado ==-1:
                    print('Desculpe, esse número de item não é válido.')
                    print('Você será redirecionado ao início')
                
                    time.sleep(2)
                    print("\033c", end="")
                    continue
            except ValueError:
                print('Informação inválida')
            
            if int(produto_selecionado) >= len(carrinho_compra_produto):
                
                print('Desculpe, esse número de item não é válido.')
                print('Você será redirecionado ao início')
                
                time.sleep(2)
                print("\033c", end="")
                continue
            print(f'Informe o que deseja alterar no produto: {carrinho_compra_produto[int(produto_selecionado)]}:')
            
            opcao_troca = input('1. Quantidade \n2. Valor\nSelecione um Item ou digite 0 para sair: ')
            
            if opcao_troca =='0':
                
                print('Você optou por sair sem alterar o produto')
                time.sleep(2)
                print("\033c", end="")
                continue
            
            elif opcao_troca == '1':
                
                try:
                    
                    quantidade_nova = int(input('Informe a quantidade: '))
                    carrinho_compra_quantidade.pop(produto_selecionado)
                    carrinho_compra_quantidade.insert(produto_selecionado,quantidade_nova)
                    print('Item Alterado com sucesso.')
                    time.sleep(2)
                    print("\033c", end="")
                    
                except ValueError:
                    
                    print('Quantidade de produto inválido')
                    print('Quantidade do produto não foi alterada.')
                    
                    time.sleep(2)
                    print("\033c", end="")
                    
            
                
            elif opcao_troca == '2':
                            
                try:
                    
                    valor_novo = float(input('Informe o novo valor: ').replace(',','.'))
                    carrinho_compra_preco.pop(produto_selecionado)
                    carrinho_compra_preco.insert(produto_selecionado,valor_novo)
                    print('Item Alterado com sucesso.')
                    time.sleep(2)
                    print("\033c", end="")
                    
                except ValueError:
                    
                    print('Valor de produto inválido')
                    print('Valor do produto não foi alterada.')
                    
                    time.sleep(2)
                    print("\033c", end="")
                    
            
                
    
    elif opcao == '6': # Validação para sair do While

        break
    
    else:
        
        print('Opção inválida.')
        
print('Obrigado. Até mais.')