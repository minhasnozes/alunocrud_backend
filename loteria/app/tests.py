from django.test import TestCase

from .models import Aluno


class AlunoModelTestCase(TestCase):
    def setUp(self):
        Aluno.objects.create(nome='João', sobrenome='Silva', data_nascimento='1991-01-01')
        Aluno.objects.create(nome='Marcus', sobrenome='Soares', data_nascimento='1991-01-01')
        Aluno.objects.create(nome='Luiz', sobrenome='Soares', data_nascimento='1991-01-01')
        Aluno.objects.create(nome='Alexandre', sobrenome='Soares', data_nascimento='2000-07-01')

        self.aluno = Aluno.objects.get(nome='João')

    def test_aluno_criado_com_sucesso(self):
        self.assertEqual(self.aluno.nome, 'João')
        self.assertEqual(self.aluno.sobrenome, 'Silva')
        self.assertEqual(self.aluno.data_nascimento.strftime('%Y-%m-%d'), '1991-01-01')

    def test_deletar_aluno(self):
        aluno = Aluno.objects.get(nome='Marcus')
        aluno.delete()
        with self.assertRaises(Aluno.DoesNotExist):
            Aluno.objects.get(nome='Marcus')

    def test_renomear_nome(self):
        self.aluno.nome = 'Joãozinho'
        self.aluno.save()
        self.assertEqual(self.aluno.nome, 'Joãozinho')

    def test_listar_alunos_nascidos_entre_data(self):
        self.list_alunos = Aluno.objects.filter(data_nascimento__range=["1990-01-01", "2000-01-01"])
        self.assertEqual(len(self.list_alunos), 3)

    def test_deletar_lote(self):
        self.alunos_soares = Aluno.objects.filter(sobrenome='Soares')
        self.alunos_soares.delete()
        self.assertEqual(len(Aluno.objects.all()), 1)
