from django.test import TestCase
from model_mommy import mommy


class EnderecoAlunoTestCase(TestCase):
    def setUp(self):
        self.endereco = mommy.make('EnderecoAluno')
    
   
class AlunoTestCase(TestCase):
    
    def setUp(self):
        self.aluno = mommy.make('Aluno')

    
class TelefoneAlunoTestCase(TestCase):
    pass


class MatriculaAlunoTestCase(TestCase):
    pass


class BoletimTestCase(TestCase):
    pass


class NotaTestCase(TestCase):
    pass

