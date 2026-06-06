
lista_numeros         = []
lista_ordenada        = []
soma_numeros          = 0
media_numeros         = 0
maior_numero          = 0
menor_numero_positivo = 9999
cont                  = 0


print('Insira uma lista de números e digite 0 quando terminar.')

while True: # Loop para pegar os números digitados pelo usuário.
    
    numero = None # Linha para zerar a configuração da validação do valor digitado para não quebrar o código
    
    numero = input('Informe um número: ')
    
    if numero == '0': # Validação para sair do loop
        break
    try:
        lista_numeros.append(int(numero))
    except:
        ...
    
   
    
for numeros in lista_numeros: # for para processamento das informações
    cont +=1          #Contador para tirar a média
    soma_numeros += numeros   #Pegar a soma dos números
    
    if numeros > int(maior_numero): # Pegar o maio número
        maior_numero = numeros
    elif numeros < menor_numero_positivo and numeros > 0: # Para calcular o menor número positivo digitado.
        menor_numero_positivo = numeros
for i in lista_numeros:
    pos = 0

    while pos < len(lista_ordenada) and lista_ordenada[pos] < i:
        pos += 1

    lista_ordenada.insert(pos, i)

        
media_numeros = soma_numeros/cont
   
   
print(f'A soma é: {soma_numeros}')
print (f'A média é: {media_numeros}')
print (f'O maior número é: {maior_numero}')
print (f'O menor número positivo é: {menor_numero_positivo}')
for i in lista_ordenada:
    print(i)
