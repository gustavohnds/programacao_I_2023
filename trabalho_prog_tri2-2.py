class Pessoa:
    def __init__(self, nome, telefone, email, cpf):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
    def __str__(self):
        return f'''
        ---- PESSOA -----
        nome: {self.nome},
        telefone: {self.telefone},
        email: {self.email},
        cpf: {self.cpf}'''
#Teste da Classe Pessoa    
nome = "Beatriz Cristina Deschamps"
telefone = "047 991099177"
email = "beatrizdeschamps59@gmail.com"
cpf = "567.654.987-09"
nova = Pessoa(nome, telefone, email, cpf)
#print(" Teste da classe Pessoa:\n", nova)

class Paciente:
    def __init__(self, nome, telefone, email, cpf, tps):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.tps = tps
    def __str__(self):
        return f'''
        ----- PACIENTE -----
        nome: {self.nome},
        telefone: {self.telefone},
        email: {self.email},
        cpf: {self.cpf},
        tps: {self.tps}'''
#Teste da Classe Paciente    
nome = "Kemilly Domingos de Souza"
telefone = "047 998786565"
email = "kemillydomingos480@gmail.com"
cpf= "123.432.987-09"
tps = "0-"
novo_paciente = Paciente(nome, telefone, email, cpf, tps)
#print("Teste da classe Paciente:\n", novo_paciente)

class Funcionario:
    def __init__(self, nome, telefone, email, cpf, codigo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.codigo = codigo
    def __str__(self):
        return f'''
        ---- FUNCIONÁRIO -----
        nome: {self.nome},
        telefone: {self.telefone},
        email: {self.email},
        cpf: {self.cpf},
        codigo: {self.codigo}''' 
#Teste da Classe Funcionario
nome = "Gustavo Henrique Nogueira do Santos"
telefone = "047 998976756"
email = "gustavoghnds@gmail.com"
cpf = "789.098.654-09"
codigo = "0612032"       
novo_funcionario = Funcionario(nome, telefone, email, cpf, codigo)
#print("Teste da classe Funcionario:\n", novo_funcionario)

class Procedimento:
    def __init__(self,paciente, funcionario, data, hora):
        self.paciente = paciente
        self.funcionario = funcionario
        self.data = data
        self.hora = hora
    def __str__(self):
        return f'''
        ---- PROCEDIMENTO -----
        paciente: {self.paciente},
        funcionario: {self.funcionario},
        data: {self.data},
        hora: {self.hora}'''
#Teste de Classe Procedimento
data = "03/05/2023"
hora = "16:20"
novo_procedimento = Procedimento(novo_paciente, novo_funcionario, data, hora)
#print("Teste da Classe Procedimentos:\n", novo_procedimento)

class Cirurgia:
    def __init__(self, paciente, funcionario, procedimento, cirurgia):
        self.paciente = paciente
        self.funcionario = funcionario
        self.procedimento = procedimento
        self.cirurgia = cirurgia
    def __str__(self):
        return f'''
        ----- CIRURGIA -----
        paciente: {self.paciente},
        funcionario: {self.funcionario},
        procedimento: {self.procedimento},
        cirurgia: {self.cirurgia}'''
#Teste da Cirurgia
cirurgia = "Cesaria"
nova_cirurgia = Cirurgia(novo_paciente, novo_funcionario, novo_procedimento, cirurgia)
print( nova_cirurgia)

#ALUNOS QUE FIZERAM O TRABALHO
#Beatriz Cristina Deschamps
#Gustavo Henrique Nogueira dos Santos
#Kemilly Domingos de Souza
#202 informática