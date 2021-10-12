class Carro:
    def __init__(self, cor, marca, ano, ligado):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.ligado = False
        
    
    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_ano(self):
        return self.ano

    def set_ano(self, ano):
        self.ano = ano

    def get_ligado(self):
        return self.ligado

    def set_cor(self, ligado):
        self.ligado = ligado

    

    def acelerar(self):
        print("Meu carro faz Darandandandan\n")

    def ligar(self,ligar):
        self.ligado = True
        print(f"{self.ligar}: {ligar}\n")

    def freiar(self):
        print(f"Ta carregando é gente ne boi não\n")
        