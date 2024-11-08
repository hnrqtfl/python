class Aluno:
    def __init__(self, nome, matricula, curso="", data_nasc=""):
        self._nome = nome
        self._matricula = matricula
        self._curso = curso
        self._data_nasc = data_nasc

@property
def nome(self):
    print(self._nome)
