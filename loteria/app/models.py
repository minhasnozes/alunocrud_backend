from django.db import models
from django.contrib.postgres.fields import ArrayField


class Concurso(models.Model):
    def __init__(self, response):
        self.acumulado = response['acumulado']
        self.dataApuracao = response['dataApuracao']
        self.dataProximoConcurso = response['dataProximoConcurso']
        self.dezenasSorteadasOrdemSorteio = response['dezenasSorteadasOrdemSorteio']
        self.exibirDetalhamentoPorCidade = response['exibirDetalhamentoPorCidade']
        self.indicadorConcursoEspecial = response['indicadorConcursoEspecial']
        self.listaDezenas = response['listaDezenas']
        self.listaDezenasSegundoSorteio = response['listaDezenasSegundoSorteio']
        self.listaMunicipioUFGanhadores = response['listaMunicipioUFGanhadores']
        self.localSorteio = response['localSorteio']
        self.nomeMunicipioUFSorteio = response['nomeMunicipioUFSorteio']
        self.nomeTimeCoracaoMesSorte = response['nomeTimeCoracaoMesSorte']
        self.numero = response['numero']
        self.numeroConcursoAnterior = response['numeroConcursoAnterior']
        self.numeroConcursoFinal_0_5 = response['numeroConcursoFinal_0_5']
        self.numeroConcursoProximo = response['numeroConcursoProximo']
        self.numeroJogo = response['numeroJogo']
        self.premiacaoContingencia = response['premiacaoContingencia']
        self.observacao = response['observacao']
        self.tipoJogo = response['tipoJogo']
        self.tipoPublicacao = response['tipoPublicacao']
        self.ultimoConcurso = response['ultimoConcurso']
        self.valorArrecadado = response['valorArrecadado']
        self.valorAcumuladoConcurso_0_5 = response['valorAcumuladoConcurso_0_5']
        self.valorAcumuladoConcursoEspecial = response['valorAcumuladoConcursoEspecial']
        self.valorAcumuladoProximoConcurso = response['valorAcumuladoProximoConcurso']
        self.valorEstimadoProximoConcurso = response['valorEstimadoProximoConcurso']
        self.valorSaldoReservaGarantidora = response['valorSaldoReservaGarantidora']
        self.valorTotalPremioFaixaUm = response['valorTotalPremioFaixaUm']

    acumulado = models.BooleanField()
    dataApuracao = models.DateField()
    dataProximoConcurso = models.DateField(null=True, blank=True)
    dezenasSorteadasOrdemSorteio = ArrayField(
        ArrayField(models.CharField(max_length=2, blank=False), size=6)
    )
    exibirDetalhamentoPorCidade = models.BooleanField()
    indicadorConcursoEspecial = models.IntegerField()
    listaDezenas = ArrayField(
        ArrayField(models.CharField(max_length=2, blank=False), size=6)
    )
    listaDezenasSegundoSorteio = ArrayField(
        ArrayField(models.CharField(max_length=2, blank=False), size=6)
    )
    listaMunicipioUFGanhadores = ArrayField(
        ArrayField(models.CharField(max_length=3, blank=False), size=6)
    )
    localSorteio = models.CharField(max_length=50, blank=True)
    nomeMunicipioUFSorteio = models.CharField(max_length=50)
    nomeTimeCoracaoMesSorte = models.CharField(max_length=50, null=True, blank=True)
    numero = models.IntegerField()
    numeroConcursoAnterior = models.IntegerField()
    numeroConcursoFinal_0_5 = models.IntegerField()
    numeroConcursoProximo = models.IntegerField()
    numeroJogo = models.IntegerField()
    premiacaoContingencia = models.TextField(null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    tipoJogo = models.CharField(max_length=50)
    tipoPublicacao = models.IntegerField()
    ultimoConcurso = models.BooleanField()
    valorArrecadado = models.FloatField()
    valorAcumuladoConcurso_0_5 = models.FloatField()
    valorAcumuladoConcursoEspecial = models.FloatField()
    valorAcumuladoProximoConcurso = models.FloatField()
    valorEstimadoProximoConcurso = models.FloatField()
    valorSaldoReservaGarantidora = models.FloatField()
    valorTotalPremioFaixaUm = models.FloatField()


class RateioPremio(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    descricaoFaixa = models.CharField(max_length=50)
    faixa = models.IntegerField()
    numeroDeGanhadores = models.IntegerField()
    valorPremio = models.FloatField()


class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False)

    def __str__(self):
        return f"{self.nome}"


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.nome}"


class Curso(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"


class AlunoCurso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
