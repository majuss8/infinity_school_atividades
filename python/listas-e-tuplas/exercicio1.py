T = ()

qtd = int(input('Quantos itens? '))

T = list(T)

for n in range(qtd):
    n = int(input('Informe os números: '))
    T.append(n)

for i in T:
    if i % 2 == 0:
        T.remove(i)

T = tuple(T)

print(T)
