from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def emitir_som(self):
        print("som indefinido")

    @abstractmethod
    def mover(self):
        print("O animal esta se movendo")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print("Au Au")

    def mover(self):
        print("O animal esta se movendo")


    def __str__(self):
       return f"Nome: {self.nome}, Idade: {self.idade} anos, Raça: {self.raca}"


class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        print("Miau Miau")
    
    def mover(self):
        print("O animal esta se movendo")

    def __str__(self):
       return f"Nome: {self.nome}, Idade: {self.idade} anos, Cor do pelo: {self.cor_pelo}"


class Passaro(Animal):
    def __init__(self, nome, idade, tam_bico):
        super().__init__(nome, idade)
        self.tam_bico = tam_bico

    def emitir_som(self):
        print("Piu Piu")

    def mover(self):
        print("O passaro esta voando")

    def __str__(self):
       return f"Nome: {self.nome}, Idade: {self.idade} anos, Tamanho do bico: {self.tam_bico}cm"



zoologico = [
    Cachorro("Rex", 3, "Golden"),
    Gato("Aya", 1, "Branco com manchas cinza"),
    Passaro("Banguela", 4, 4)
]

for animal in zoologico:
    print(animal)
    animal.emitir_som()
    animal.mover()
