from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models

from .models import Aluno, EnderecoAluno, TelefoneAluno, MatriculaAluno, Boletim, Nota


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('frist_name', 'last_name', 'cpf', 'nascimento', 'email', 'sexo')


@admin.register(EnderecoAluno)
class EnderecoAlunoAdm(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'cidade', 'estado', 'cep')


@admin.register(TelefoneAluno)
class TelefoneAlunoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'ddd', 'numero', 'contato')


@admin.register(MatriculaAluno)
class MatriculaAlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'data_matricula', 'aluno')


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    list_display = ('nome_boletim','nome_turma', 'Matricula_aluno', 'aprovado')


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('nome_materia', 'nome_professor', 'trimestre', 'trabalhos_nota', 'prova_nota', 'total')