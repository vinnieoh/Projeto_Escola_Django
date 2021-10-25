from django.db import models
from django.db.models.fields import DateField


class EnderecoAluno(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=200, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)

    class Meta:
        verbose_name = 'Endereço Aluno'
        verbose_name_plural = 'Endereços Alunos'

    def __str__(self) :
        return f'Rua: {self.rua}'


class Aluno(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    nascimento = DateField(null=False, blank=False)
    email = models.EmailField(max_length=250, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100)

    sexo_choice = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções"),
    )

    sexo = models.CharField(max_length=1, choices=sexo_choice, blank=False, null=False)
    endereco_aluno = models.OneToOneField(EnderecoAluno, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f"{self.frist_name} {self.last_name}"


class TelefoneAluno(models.Model):
    aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE, related_name='contato')
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=9)

    tipo_contato = (
        ("CEL", "Celular"),
        ("TEL", "Telefone"),
    )

    contato = models.CharField(max_length=3, choices=tipo_contato, blank=False, null=False)

    def __str__(self):
        return f'({self.ddd}) {self.numero}'


class MatriculaAluno(models.Model):
    matricula = models.CharField(max_length=100, unique=True, null=False, blank=False)
    data_matricula = models.DateTimeField(auto_now_add=True)
    aluno = models.OneToOneField(Aluno, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.matricula}'

    
class Boletim(models.Model):
    nome_boletim = models.CharField(max_length=100)
    nome_turma = models.CharField(max_length=50)
    Matricula_aluno = models.ForeignKey("MatriculaAluno", on_delete=models.CASCADE, related_name='boletim')
    aprovado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nome_boletim}'


class Nota(models.Model):
    nome_materia = models.CharField(max_length=20, null=False, blank=False)
    nome_professor = models.CharField(max_length=100, null=False, blank=False)

    provas_trimestre = (
        ("1Tri", "1-Trimestre"),
        ("2Tri", "2-Trimestre"),
        ("3Tri", "3-Trimestre"),
    )

    trimestre = models.CharField(max_length=4, choices=provas_trimestre, blank=False, null=False)
    trabalhos_nota = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)
    prova_nota = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)
    total = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)


    def __str__(self) -> str:
        return f'Materia: {self.nome_materia} | Trimestre: {self.trimestre}'
