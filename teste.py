lista_produto = ('Arroz','feijão','Carne', 'macarrão')
lista_preco   = (15,50,12.50,100)
quantidade    = (1,2,3,10)

print(f"   {'ITEM':<6} {'PRODUTO':<16} {'QTD':<3} {'VALOR':>14}")
print("-" * 50)
for i in range(len(lista_produto)):
    print(f'    {i:.<4} {lista_produto[i]:.<17}{quantidade[i]:.<14}{lista_preco[i]:4.2f}')
print("-" * 50)
    