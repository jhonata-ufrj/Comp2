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
    """Representa o conceito de uma Turma"""
    #Construtor que aproveita atributos da classe Pai e adiciona novos atributos
    def __init__(self, nome, carga, vagas, horario, alunos = []):
        super().__init__(nome, carga, vagas)
        self.horario = horario
        self.alunos = alunos

    #Método especial que soma dois objetos caso os parâmetros comparados no IF sejam iguais
    def __add__(self, obj):
        if(self.nome == obj.nome and self.carga == obj.carga and self.horario == obj.horario):
            novo = Turma(self.nome, self.carga, self.vagas + obj.vagas, self.horario, 
            self.alunos + obj.alunos )
            return novo
        else:
            string = "Não foi possível juntar as turmas. "
            if(self.nome != obj.nome): 
                string += "Nomes têm que ser iguais. " 
            if(self.carga != obj.carga):
                string += "Cargas têm que ser iguais. "
            if(self.horario != obj.horario):
                string += "Horários têm que ser iguais"
            return string    

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}, carga: {}, horario: {}\nvagas totais: {}, vagas livres: {}".format(self.nome,
        self.carga, self.horario, self.vagas, self.vagas - len(self.alunos))


#Questão 2
class Bolsista(Aluno):
    """Representa o conceito de um Bolsista"""
    #Construtor que aproveita atributos da classe Pai e adiciona um novo atributo
    def __init__(self, nome, DRE, bolsa):
        super().__init__(nome, DRE)
        self.bolsa = bolsa

    #Método que muda o Status da matrícula para Trancado e zera a bolsa do monitor
    def trancarMatricula(self):
        super().trancarMatricula()
        self.bolsa = 0




