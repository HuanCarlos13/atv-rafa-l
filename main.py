from Carro import Carro
from Pessoa import Pessoa
from Animal import Animal

# instancias 
Animal = Animal("Branca","vira lata", "Cachorro")
Carro = Carro("preto", "toyota", 2016, "ligado")
Pessoa = Pessoa("Irineu", 18, 1.89)

#Metodo - Carro
print("===Carro===")
Carro.acelerar()
Carro.freiar()
ligar = int(input(f"Digite o numero de vezes que o carro ligou:  "))
Carro.ligar(ligar)

#Metodo - Pessoa
print("===Pessoa===\n")
Pessoa.pular()
Mensagem = input(f"Eu quis dizer que {Pessoa.get_nome()}: ")
Pessoa.falar(Mensagem)
Pessoa.andar()

#Metodo - Animal
print("===Animal===\n")
Animal.macaco()
Animal.latir()
msg = int(input(f"Digite o Numero de patas: "))
Animal.patas(msg)




