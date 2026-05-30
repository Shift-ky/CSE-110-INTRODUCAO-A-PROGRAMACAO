'''
Escreva um programa que determine a nota conceitual (A, B, C, D, F) de um curso de acordo com a seguinte escala:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60

Além disso, exiba uma mensagem para o usuário informando se ele foi aprovado no curso ou não (para ser aprovado no curso é necessário pelo menos 70%).
'''


nota = float(input('Digite a nota: '))

if nota >= 90:
    print('A')
elif nota>=80:
    print('B')
elif nota>=70:
    print('B')
elif nota>=60:
    print('B')
else:
    print('60')
    

if nota >= 70:
    print("Parabéns! Você passou na disciplina!")
else:
    print("Você conseguirá na próxima vez!")
    

print(nota % 10)