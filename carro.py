class Casa:

    def __init__(self, cor, num_quartos, tamanho_m2, valor):
        self.cor = cor
        self.num_quartos = num_quartos
        self.tamanho_m2 = tamanho_m2
        self._valor = valor
    
    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"A casa foi pintada de {self.cor}.")

    def reformar(self, tamanho_m2):
        self.tamanho_m2 = tamanho_m2
        print(f"A casa foi reformada para {self.tamanho_m2} metros quadrados.")

    def valorizar(self, valor):
        self.valor = valor
        print(f"O valor da casa agora é R$ {self.valor}.")

casa = Casa("cor - azul", "3 quartos", "40m2" , "300000R$")\

print(casa.cor)
print(casa.num_quartos)
print(casa.tamanho_m2)
print(casa._valor)



class Carro:

    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano
        self._placa = placa
        
    def ligar(self):
        print(f"O carro {self.marca} {self.modelo} está ligado.")

    def desligar(self):
        print(f"O carro {self.marca} {self.modelo} está desligado.")
    
    def _placa(self):
        return self._placa
    
carro = Carro("marca - Toyota", "modelo - Corolla", "ano - 2020" , "placa - ABC-1234")

print(carro.marca)
print(carro.modelo)
print(carro.ano)
print(carro._placa)
print(carro.ligar)



class Fogao:
    
    def __init__(self, marca, num_bocas, tipo, numero_serie):
        self.marca = marca
        self.num_bocas = num_bocas
        self.tipo = tipo #gas ou eletrico
        self._numero_serie = numero_serie

    def ligar(self):
        print(f"O fogão {self.marca} está ligado.")

    def desligar(self):
        print(f"O fogão {self.marca} está desligado.")

    def _numero_serie(self):
        return self._numero_serie
    
fogao = Fogao("marca - Brastemp", "4 bocas", "tipo - eletrico" , "numero de serie - 123456")

print(fogao.marca)
print(fogao.num_bocas)
print(fogao.tipo)
print(fogao._numero_serie)
