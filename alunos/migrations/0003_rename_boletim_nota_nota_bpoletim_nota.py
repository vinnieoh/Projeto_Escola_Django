# Generated by Django 3.2.10 on 2022-02-01 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_rename_boletim_nota_boletim_nota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='Boletim_nota',
            new_name='Bpoletim_nota',
        ),
    ]
