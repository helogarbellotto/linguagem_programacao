class Aluno:

    def __init__(self, nome, matricula, nav1, nav2, ntrabalho):
        self.nome = nome
        self.matricula = matricula
        self.nav1 = nav1
        self.nav2 = nav2
        self.ntrabalho = ntrabalho

    def resultado(self):
        media = (self.nav1 + self.nav2 + self.ntrabalho) / 3
        if media <4.0 :
            return "O aluno está reprovado."
        elif media <= 7.0 :
            return "O aluno está aprovado."
        else:
            return f"final: (10.0 - media: .2f)"
        
    name = input('Digite seu nome: ')
    matricula = int(input('Qual sua matrícula: '))
    nav1 = int(input('Nota da AV1: '))
    nav2 = int(input('Nota da AV2: '))
    ntrabalho = int(input('Nota do trabalho: '))


aluno = Aluno(name, matricula, nav1, nav2, ntrabalho)
print(f"Resultado do aluno {aluno.nome}: {aluno.resultado()}")



    