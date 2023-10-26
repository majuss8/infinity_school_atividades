num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

soma = num1 + num2

if soma > 20:
    resultado = soma + 8
    print(f'{soma} + 8 = {resultado}')
else:
    resultado = soma - 5
    print(f'{soma} - 5 = {resultado}')

    