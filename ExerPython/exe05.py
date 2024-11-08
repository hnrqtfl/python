'''Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B.'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))

if n1%n2 ==0:
    print(f"Os números {n1} e {n2} são divisíveis")
elif n1:
    print(f"Os números {n1} e {n2} não são divisíveis") 
