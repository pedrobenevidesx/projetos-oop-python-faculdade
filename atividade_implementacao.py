#Crie uma classe Funcionário, uma classe Analista , uma classe Gerente e Uma classe Supervisor. 
#Todas as classes devem ter os seguintes atributos:
#•	Nome;
#•	Setor;
#•	Salário;
#•	Bônus;
#Salário:
#•	Analistas: salário fixo;
#•	Gerente: R$ 90,00 por hora trabalhada sendo que o limite mensal de horas trabalhadas deverá ser de 240 horas;
#•	Supervisor: salário fixo + ajuda de custo de R$300,00
#Bônus:
#•	Analistas: 15% do salário;
#•	Supervisor: 20% do salário;
#•	Gerente: 50% do salário + 5% do total vendido;

#implemente uma classe que consiga calcular o valor total a ser pago pelos colaboradores. Tendo como exemplo: 240horas de trabalho para o gerente e R$600.000,00 de faturamento. 





class Funcionario:
    
    def __init__(self, nome, setor, salario, bonus = 0):
        self.nome = nome
        self.setor = setor
        self.salario = salario
        self.bonus = bonus

    def pagamento(self):
        return self.salario + self.bonus 
    

class Analista(Funcionario):
    def __init__(self, nome, setor, salario = 1500, bonus = 0.15):
         super().__init__(nome, setor,salario, bonus)
         self.salario = salario

    def pagamento(self):
        return self.salario + (self.salario * self.bonus)
    
    def __str__ (self):
        return f" NOME: {self.nome}\n SETOR: {self.setor}\n SALARIO BASE: {self.salario}\n SALARIO COM BONUS: {self.pagamento()} "

        


class Gerente(Funcionario):
    def __init__(self, nome, setor, horas_trabalhadas = 0, limite_horas = 240):
        self.horas_trabalhadas = horas_trabalhadas
        self.limite_horas = limite_horas
        self.valor_hora = 90
        self.bonus = 0
        super().__init__(nome, setor, 0, 0)

    def pagamento(self):
        horas = min(self.horas_trabalhadas, self.limite_horas)
        self.salario = horas * self.valor_hora
        self.bonus = self.salario * 0.50
        return self.salario + self.bonus
    
    def __str__ (self):
        salario_total = self.pagamento()
        return f" NOME: {self.nome}\n SETOR: {self.setor}\n VALOR POR HORA: {self.valor_hora}\n HORAS TRABALHADAS: {self.horas_trabalhadas}\n SALARIO: {self.salario}\n SALARIO COM BONUS: {salario_total}"



class Supervisor(Funcionario):
    def __init__(self, nome, setor, ajuda_custo = 300):
        self.ajuda_custo = ajuda_custo
        super().__init__(nome, setor, 5000)

    def pagamento(self):
        self.ajuda = self.salario + self.ajuda_custo
        bonus = self.salario * 0.20
        return self.ajuda + bonus
    
    def __str__ (self):
        return f" NOME: {self.nome}\n SETOR: {self.setor}\n AJUDA DE CUSTO: {self.ajuda_custo}\n SALARIO BASE: {self.salario}\n SALARIO TOTAL(bonus 20%): {self.pagamento()}"
    

class FolhaPagamento:
        def __init__(self):
            self.funcionarios = []

        def adicionar_funcionario(self, funcionario):
            self.funcionarios.append(funcionario)

        def gastos_totais(self):
            total = 0
            for f in self.funcionarios:
                total += f.pagamento()
            return total
        
        def __str__ (self):
            return f"GASTOS TOTAIS: {self.gastos_totais()}"
        

analista = Analista("Marco Paulo", "Analista")
print(analista)
    


supervisor = Supervisor("Pedro Henrique", "Supervisor")
print(supervisor)


gerente = Gerente("Maria Fernanda", "Gerente", 240)
print(gerente)



folhapagamento = FolhaPagamento()

folhapagamento.adicionar_funcionario(analista)
folhapagamento.adicionar_funcionario(supervisor)
folhapagamento.adicionar_funcionario(gerente)



print(folhapagamento)





        
        

        