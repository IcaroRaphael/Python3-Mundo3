"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = list()
for c in range(0, 5):
    lista.append(int(input("Insira o valor: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
print(f"O maior número é {maior}, e foi encontrado nas posições ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end="")
print(f"\nO menor número é {menor}, e foi encontrado nas posições ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end="")
