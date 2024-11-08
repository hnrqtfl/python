'''Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos.'''

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digiteo terceiro número "))

#Somando os números
soma = n1 + n2 + n3
print(f"A soma dos números é: {soma}")
#Fazendo divisão dos números
media = soma/3
print(f"A média dos números é: {media}")
#Fazendo a multiplicação dos números
produto = n1*n2*n3
print(f"O produto dos números acima é: {produto}")


