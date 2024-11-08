'''Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato'''
    
menu = '''
   Selecione:
   [s] Sacar
   [d] Depositar
   [e] Extrato
   [x] Sair
'''
saldo = 0
quant_saque = 3
value_saque = 0
value_dep = 0 
ext = 0

while True:
    opcao = input (menu)
    if opcao == 'x': break
    if opcao == 's': 
        value_saque = float(input("Digite o valor do saque: R$"))
        if value_saque <= saldo:
            saldo -= value_saque
            print (f"Saque de R${value_saque} realizado com sucesso!\nSaldo: R${saldo}")
        elif value_saque > 500:
                print("Limite de R$ 500 atingido")
        else:
            print("Saldo indisponível")
    if opcao == 'd':
        value_saque = float(input("Digite o valor do depósito: R$"))
        if value_dep > 0:
              saldo += value_dep
              print(f"Depósito de R${value_dep} realizado com sucesso!\nSaldo: R${saldo}")
    if opcao == 'e':
        ext = print(f"Saques: R${value_saque}\nDepósitos: R${value_dep}\nSaldo atual: R${saldo}")
        if value_dep == 0:
              print(f"Nenhuma movimentação feita")