'''Faça um algoritmo para ler três números e imprimir o maior.'''

n1 = int(input(f"Digite um número:"))
n2 = int(input(f"Digite o segundo número:"))
n3 = int(input(f"Digite o terceiro número:"))

if n1 > n2 > n3:
    print(f"O maior número é: ", n1)
if n1 < n2 > n3:
    print(f"O maior número é: ", n2)
if n1 < n2 < n3:
    print(f"O maior número é: ", n3)
elif n1 == n2 == n3:
    print("Os três números são iguais")

