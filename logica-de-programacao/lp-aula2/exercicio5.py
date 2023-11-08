num = int(input('Digite um número: '))

if num % 3 == 0 and num % 7 == 0:
    print('É divisível por 3 e por 7')
elif num % 3 == 0:
    print('É divisível por 3')
elif num % 7 == 0:
    print('É divisível por 7')
else:
    print('Não é divisível nem por 3 nem por 7')

