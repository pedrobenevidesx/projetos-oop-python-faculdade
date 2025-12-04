
class Casa:
    def __init__(self, cor, num_quartos, tamanho_m2, valor):
        self.cor = cor
        self.num_quartos = num_quartos
        self.tamanho_m2 = tamanho_m2
        self._valor = valor  

    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"A casa foi pintada de {self.cor}.")

    def reformar(self, acrescimo_m2):
        self.tamanho_m2 += acrescimo_m2
        print(f"A casa foi reformada, agora tem {self.tamanho_m2} m².")

    def _valorizar(self, acrescimo_valor):  
        self._valor += acrescimo_valor
        print(f"O valor da casa aumentou para R$ {self._valor}.")

    def __str__(self):
        return f"Casa: {self.cor}, {self.num_quartos} quartos, {self.tamanho_m2} m², valor R$ {self._valor}"



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

    def _mostrar_placa(self):  
        return self._placa

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, ano {self.ano}, placa {self._placa}"



class Fogao:
    def __init__(self, marca, num_bocas, tipo, numero_serie):
        self.marca = marca
        self.num_bocas = num_bocas
        self.tipo = tipo
        self._numero_serie = numero_serie

    def ligar(self):
        print(f"O fogão {self.marca} está ligado.")

    def desligar(self):
        print(f"O fogão {self.marca} está desligado.")

    def _mostrar_numero_serie(self):  
        return self._numero_serie

    def __str__(self):
        return f"Fogão: {self.marca}, {self.num_bocas} bocas, {self.tipo}, Nº de série: {self._numero_serie}"



casa = Casa("azul", 3, 40, 300000)
print(casa)
casa.pintar("vermelha")
casa._valorizar(50000)

carro = Carro("Toyota", "Corolla", 2020, "ABC-1234")
print(carro)
carro.ligar()
print("Placa privada:", carro._mostrar_placa())

fogao = Fogao("Brastemp", 4, "elétrico", "123456")
print(fogao)
fogao.ligar()
print("Número de série privado:", fogao._mostrar_numero_serie())
