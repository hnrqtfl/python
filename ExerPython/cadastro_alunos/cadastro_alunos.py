'''Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola.
O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.
Organize o código em funções.
'''
alunos = {}
def menu():
    menu_principal = '''
    =========================
        Menu Principal:
        1. Cadastrar Aluno
        2. Consultar Aluno
        3. Excluir Aluno
        4. Sair
    =========================    
    '''
    print(menu_principal)
def escolher_opcao():  
    while True:
        opcao = int(input("Digite uma opção"))
        match(opcao):
              case 1:
                  cadastrar_aluno()
              case 2:
                  consultar_aluno()
              case 3:
                  excluir_aluno()
              case 4:
                  break                  
              case _:
                  print("Opção inválida")

def cadastrar_aluno():
        aluno = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        curso = input("Digite o curso do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/yyyy): ")
        print(f"Aluno {aluno} cadastrado com sucesso!")
        alunos[matricula] = {"nome": aluno, "curso": curso, "data_nascimento": data_nascimento}
        return alunos
def consultar_aluno():
        buscar_matrícula = input("Digite a matrícula do aluno:")
        if buscar_matrícula in alunos:
               aluno_encontrado = alunos[buscar_matrícula]
               print(f"Aluno encontrado: {alunos}")
               print(f"Matrícula do aluno {alunos}:")
        else:
            print("Aluno não encontrado!")
def excluir_aluno():
        matricula = input("Digite a matrícula do aluno que deseja excluir:")                
        
