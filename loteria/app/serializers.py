from rest_framework import serializers

from loteria.app.models import Concurso, Aluno, Categoria, AlunoCurso, Curso


class ConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concurso
        fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class AlunoCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.CharField(source='aluno.nome')
    curso = serializers.CharField(source='curso.nome')
    class Meta:
        model = AlunoCurso
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nome')

    class Meta:
        model = Curso
        fields = '__all__'
