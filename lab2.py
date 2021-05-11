#Nome: Jhonata Oliveira da Silva
#DRE: 118153533

from datetime import date

class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        """Cria um objeto da classe Aluno com atributos nome, DRE, matricula"""
        self.nome = nome
        self.DRE = DRE       
        self.matricula = matricula

    def trancarMatricula(self):
        """Tranca a matricula"""
        self.matricula = "trancada"

    def cancelarMatricula(self):
        """Cancela a matricula"""
        self.matricula = "cancelada"

    def reativarMatricula(self):
        """Reativa a matricula se a matricula não for cancelada"""
        if self.matricula == "cancelada":
            print("Matrícula cancelada, solicite reabertura de matrícula")
        else:
            self.matricula = "ativa"
            
    def dados(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

    def __str__(self):
        return "{} {} matricula {}".format(self.nome, self.DRE, self.matricula)

#=======================================

class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, vagas = 0):
        """Cria um objeto da classe com atributos nome, vagas, alunos"""
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        """Junta duas disciplinas se o nome delas for idêntico"""
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")
    
    def inscreverAluno(self, aluno):
        """Inscreve um objeto da classe Aluno na disciplina se tiver
        vagas livres ou o Aluno não for ainda inscrito na disciplina"""
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:
            print("Vagas esgotadas")
    
    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        if len(self.alunos) == 0:
            return "{}, sem alunos inscritos.\nVagas totais: {}. Vagas livres: {}".format(self.nome,
            self.vagas, self.vagas)
        else:
            string_out = "{}, alunos inscritos:\n".format(self.nome)
            for aluno in [str(aluno) + '\n' for aluno in self.alunos]:
                string_out += aluno 
            string_out += "Vagas totais: {}. Vagas livres: {}".format(self.vagas,
            self.vagas - len(self.alunos))
            return string_out     
            

    def consultarVagas(self):
        """Retorna a quantidade de vagas """
        return "Vagas totais: {}. Vagas livres: {}".format(self.vagas, self.vagas - len(self.alunos))


#Questão 1
MAB241 = Disciplina("Computação II", 20)
aluno1 = Aluno("Jhon", 118153)
aluno2 = Aluno("Conrado", 131313)
aluno3 = Aluno("Felipe", 171717)
MAB241.inscreverAluno(aluno1)
MAB241.inscreverAluno(aluno2)
MAB241.inscreverAluno(aluno3)
print(MAB241.consultarVagas())
print(MAB241)


#Questão 2
class Pessoa:
    """Classe que representa uma pessoa com alguns atributos relacionados a data"""
    def __init__(self, nome, dataNascimento, nomeDeMae, nomeDePai):
        """Cria um objeto da classe Pessoa com atributos nome, Data de nascimento,
        nome da mãe e do pai"""
        self.nome = nome 
        self.dataNascimento = dataNascimento
        self.nomeDeMae = nomeDeMae
        self.nomeDePai = nomeDePai

    def idade(self, data = date.today().strftime("%d/%m/%Y")):
        """Calcula a idade da pessoa em anos com base na sua Data de nascimento e o dia atual"""
        self.data = data
        anos = (int(self.transformaData(self.data)) - int(self.transformaData(self.dataNascimento)) ) / 365
        return int(anos) 
        

    def transformaData(self,datx):
        """ Transforma a Idade passada em dd/mm/aaaa em dias"""
        self.datx = datx
        return int(self.datx[0:2]) + (int(self.datx[3:5]))* 30 + (int(self.datx[6:10])) * 365

    def __str__(self):
        """Retorna o nome, a idade em anos e o nome dos pais"""     
        return "nome: {}, idade: {}, mae: {}, pai: {}".format(self.nome, self.idade(),
        self.nomeDeMae, self.nomeDePai)

pessoa1 = Pessoa("Jhonata", "28/01/1999", "Rosalia", "Claudio")
print(pessoa1) 

