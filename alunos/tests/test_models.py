from django.test import TestCase
from model_bakery import baker

from alunos.models import EnderecoAluno

class EnderecoAlunoTestCase(TestCase):
    
    def setUp(self):
       self.endereco = baker.make('EnderecoAluno')

    
    
   
class AlunoTestCase(TestCase):
    
    def setUp(self):
        ...

    
class TelefoneAlunoTestCase(TestCase):
    pass


class MatriculaAlunoTestCase(TestCase):
    pass


class BoletimTestCase(TestCase):
    pass


class NotaTestCase(TestCase):
    pass

