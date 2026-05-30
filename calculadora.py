'''
@Author Robson Paiva
@date 14/05/2026
'''
# Solicitação dos dados ao usuário
refeicao_cianca   = float(input('Qual é o preço da refeição de uma criança? '))
refeica_aduto     = float(input('Qual é o preço da refeição de um adulto? '))
valor_bebidas     = float(input('valor da bebida ? '))
valor_sobremessa  = float(input('Valor sobremessa ? '))
qtd_crianca       = int(input('Há quantas crianças? '))
qtd_adulto        = int(input('Há quantos adultos? '))
qtb_bebidas       = int(input('Quantidade de bebida? '))
qtd_sobremessa    = int(input('Quantidade sobremessa ? '))


print()

# Calculo para obter o subtotal
subtotal =  (refeicao_cianca  * qtd_crianca) + \
            (refeica_aduto    * qtd_adulto)  + \
            (valor_bebidas    * qtb_bebidas) + \
            (valor_sobremessa * qtd_sobremessa)

print(f'subtotal: R$ {subtotal:.2f}')
print()

taxa = float(input('Qual é a taxa de imposto sobre vendas? '))

#calculo para obter o valor da taxa de serviço
valor_taxa = (taxa / 100) * subtotal

total = valor_taxa + subtotal
print()
print(f'Imposto sobre Vendas: R$ {valor_taxa:.2f}')
print(f'Total: R$ {total:.2f}')
print()

pagamento = float(input('Qual é o valor do pagamento? '))

#Calculo do troco
troco = pagamento - total
print()
print(f'Troco: R$ {troco:.2f}')