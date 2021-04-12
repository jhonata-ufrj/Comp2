#Nome: Jhonata Oliveira da Silva
#DRE: 118153533

# AULA 3
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
            
    def __str__(self): # método novo
        """Retorna uma descrição de um objeto da classe"""
        return "{}, DRE {}, matricula {}\n".format(self.nome, str(self.DRE), self.matricula)


class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, carga, vagas = 40):
        self.nome = nome
        self.carga = carga
        self.vagas = vagas
    
    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return self.nome
    
#  Herança ================================

class Monitor(Aluno):
    """Representa o conceito de um monitor"""
    def __init__(self, nome, DRE, historico = []):
        """O parametro historico deve ser uma lista de listas, onde o primeiro
        elemento da sublista é uma disciplina e o segundo elemento é o período."""
        super().__init__(nome, DRE)
        self.historico = historico

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        string =  Aluno.__str__(self) + "HISTÓRICO DE MONITORIA\n"
        string += "Nome da Disciplina\tCarga horária\tPeríodo de monitoria\n"
        for entrada in self.historico:
            turma = entrada[0]
            periodo = entrada[1]
            string += "{}\t\t{}\t\t{}\n".format(turma.nome, turma.carga, periodo)
        return string
               
#Questão 1
class Turma(Disciplina):
    def __init__(self, nome, carga, vagas, horario, alunos = []):
        super().__init__(nome, carga, vagas)
        self.horario = horario
        self.alunos = alunos

    def __add__(self, obj):
        if(self.nome == obj.nome and self.carga == obj.carga and self.horario == obj.horario):
            novo = Turma(self.nome, self.carga, self.vagas + obj.vagas, self.horario, 
            self.alunos + obj.alunos )
            return novo
        else:
            return "Não foi possív"    

    def __str__(self):
        return "{}, carga: {}, horario: {}\nvagas totais: {}, vagas livres: {}".format(self.nome,
        self.carga, self.horario, self.vagas, self.vagas - len(self.alunos))


#Questão 2
class Bolsista(Aluno):
    def __init__(self, nome, DRE, bolsa):
        super().__init__(nome, DRE)
        self.bolsa = bolsa

    def trancarMatricula(self):
        super().trancarMatricula()
        self.bolsa = 0

#fulano = Aluno("Adam", 123)
#fulana = Aluno("Eva", 111)
#mab241 = Turma("Computação II", 60, 30, "Ter 8 - 10")
#mab242 = Turma("Computação II", 60, 30, "Ter 8 - 10", [fulano])
#mab200 = Turma("Algebra I", 80, 100, "Qua 10-12", [fulano, fulana])
#print(fulana)
#print(mab241)
#print(mab200)
#o = mab241 + mab242
#print(o)
#monitor1 = Monitor("Adam", 123, [[mab241, "2020-2"],[mab200, "2021-1"]])

bolsista1 = Bolsista("Adam", 456, 1200)
print(bolsista1)

bolsista1.trancarMatricula()
print(bolsista1)
