from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from loteria.app.models import Concurso, Aluno, Categoria, Curso, AlunoCurso
from loteria.app.serializers import ConcursoSerializer, AlunoSerializer, CategoriaSerializer, CursoSerializer, \
    AlunoCursoSerializer
import requests

CONSTANT_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/{id}"


class ConcursoViewSet(viewsets.ModelViewSet):
    queryset = Concurso.objects.all()
    serializer_class = ConcursoSerializer

    @action(methods=['get'], detail=False)
    def buscar_na_loteria(self, request):
        # for id in range(10):
        resp = requests.get(CONSTANT_URL.format(id=1), verify=False)
        print(resp.json())
        concurso = Concurso(resp.json())
        print(concurso)
        concurso.save()
        data = []
        return Response(data, status=status.HTTP_200_OK)


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AlunoCursoViewSet(viewsets.ModelViewSet):
    queryset = AlunoCurso.objects.all()
    serializer_class = AlunoCursoSerializer
