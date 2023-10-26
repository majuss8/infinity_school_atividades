pesoPeixe = float(input('Digite o peso de peixes pescados: '))

if pesoPeixe > 50:
    excesso = pesoPeixe - 50
    multa = excesso * 4.00
    print(f'Peso: {pesoPeixe} Kg\nExcesso: {excesso} Kg\nA multa será de R$ {multa}')
else:
    print(f'Peso: {pesoPeixe} Kg\nNão foi excedido o limite, logo não haverá multa.')





