lista = [1,2,6,9,5,2]

set = set(lista)
print(type(set))

x = set.pop()
print(x)
print(set)

if 9 in set:
    print(f'{set} \nO 9 está contido')
else:
    print(f'{set} \nO 9 não está contido')

set.add(10)
print(set)

set.pop(5)
print(set)

set2 = set.copy()



