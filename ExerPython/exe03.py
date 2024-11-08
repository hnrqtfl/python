'''Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais.'''

n1 = float(input(f"Digite um número: "))
n2 = float(input(f"Digite o segundo número: "))
 
if n1 > n2:
    print(f"O maior número é: {n1}")
if n1 < n2:
    print(f"O menor número é: {n1}")
elif n1 == n2:
    print(f"Os números são iguais")

