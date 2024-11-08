class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("bi bi bi")
    def parar(self):
        print("Parou")
    def correr(self):    
        print("Correu")
    def __str__(self) -> str:
        return f"A bicicleta do modelo {self.modelo} da cor {self.cor} custa {self.valor}"

bicicleta_1 = Bicicleta("Vermelho", "Monark", 2008, 500)
bicicleta_2 = Bicicleta("Preto", "Caloi", 2004, 350)
bicicleta_1.buzinar()

bicicleta_2.correr()
print(bicicleta_1)
print(bicicleta_2)