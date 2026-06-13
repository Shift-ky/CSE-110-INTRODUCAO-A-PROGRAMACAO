# para a parte criativa adicionei um menu, para que possa ser visto por ano ou país

print('Informe a análise que quer fazer \n1. Por Ano\n2. Pais\n3. Ano e Pais')
opcao = '3'
ano_solicitado = '1994'
pais ='Brasil'


# Bloco de variáveis para montar a lógica das solicitações com a data informada
maior_expectativa            = '0' 
expectativa_maior_pais       = ''
menor_expectativa            = '9999'
expectativa_menor_pais       = ''
contador_ano                 = 1
soma_ano                     = 1
media_ano                    = 0
#---------------------------------------#
maior_expectativa_geral      = '0'
menor_expectativa_geral      = '999999'
ano_maior_expectativa        = ''
ano_menor_expectativa        = ''

expectativa_maior_pais_geral = ' '
expectativa_menor_pais_geral = ' '
saida = ''


with open ("expectativa-de-vida.csv", 'r', encoding='utf-8') as arquivos:
    next(arquivos)
    
    for linha in arquivos:
        linha_limpa = linha.strip()
        linha_separada = linha.split(',')
        
        entidade         = linha_separada[0].strip()
        codigo           = linha_separada[1].strip()
        ano              = linha_separada[2].strip()
        expectativa_vida = linha_separada[3].strip()
            
        if expectativa_vida > maior_expectativa_geral: # pegar a análise em geral
            maior_expectativa_geral      = expectativa_vida
            expectativa_maior_pais_geral = entidade
            ano_maior_expectativa = ano
             
        if expectativa_vida < menor_expectativa_geral: # pegar a análise em geral
            menor_expectativa_geral = expectativa_vida
            expectativa_menor_pais_geral = entidade
            ano_menor_expectativa = ano
        
        if opcao =='1':
            saida = ''
            
            if ano_solicitado == ano: # Bloco de código para pegar as informações vinda da data que o usuário digitou
                contador_ano += 1
                soma_ano += float(expectativa_vida)
                
                if expectativa_vida > maior_expectativa:
                    maior_expectativa = expectativa_vida
                    expectativa_maior_pais = entidade
                    
                if expectativa_vida < menor_expectativa:
                    menor_expectativa = expectativa_vida
                    expectativa_menor_pais = entidade
            saida += f'Para o ano de {ano_solicitado}\n'
            saida += f'A média da expectativa de vida em todos os países era de {soma_ano/contador_ano:.2f}\n'
            saida += f'A expectativa de vida máxima estava em {expectativa_maior_pais}, com {maior_expectativa}.\n'
            saida += f'A expectativa de vida mínima estava em {expectativa_menor_pais}, com {menor_expectativa}.\n'
                
        elif opcao == '2':
            saida = ''
            if pais == entidade:
                        
                contador_ano += 1
                soma_ano += float(expectativa_vida)
                    
                if expectativa_vida > maior_expectativa:
                    maior_expectativa = expectativa_vida
                    expectativa_maior_pais = entidade
                        
                if expectativa_vida < menor_expectativa:
                    menor_expectativa = expectativa_vida
                    expectativa_menor_pais = entidade
            saida += f'Para o Pais {pais}\n'
            saida += f'A média da expectativa de vida é de {soma_ano/contador_ano:.2f}\n'
            saida += f'A expectativa de vida máxima no {expectativa_maior_pais}, é {maior_expectativa}.\n'
            saida += f'A expectativa de vida mínima no {expectativa_menor_pais}, é {menor_expectativa}.\n'
        
        elif opcao =='3':
            saida = ''
            
            if pais == entidade and ano_solicitado == ano:
                        
                contador_ano += 1
                soma_ano += float(expectativa_vida)
                    
                if expectativa_vida > maior_expectativa:
                    maior_expectativa = expectativa_vida
                    expectativa_maior_pais = entidade
                        
                if expectativa_vida < menor_expectativa:
                    menor_expectativa = expectativa_vida
                    expectativa_menor_pais = entidade
            saida += f'Para o País {pais} no ano de {ano}\n'
            saida += f'A média expectativa de vida em todos o países era de {soma_ano/contador_ano:.2f}\n'
            saida += f'A expectativa de vida máxima estava no {expectativa_maior_pais}, é {maior_expectativa}.\n'
            saida += f'A expectativa de vida mínima estava no {expectativa_menor_pais}, é {menor_expectativa}.\n'
        else:
            print('Opção inválida')
            
                
                

print()
print(f'A expectativa de vida máxima geral é: {maior_expectativa_geral} de {expectativa_maior_pais_geral} em {ano_maior_expectativa}.')
print(f'A expectativa de vida mínima geral é: {menor_expectativa_geral} da {expectativa_menor_pais_geral} em {ano_menor_expectativa}.')
print(saida)

            
       
    