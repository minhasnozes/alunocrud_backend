from django.db import models


class concurso(models.Model):
    acumulado = models.BooleanField()
    dataApuracao = models.DateField()
    dataProximoConcurso = models.DateField(null=True, blank=True)
    dezenasSorteadasOrdemSorteio = models.ArrayField(models.Integer())
    exibirDetalhamentoPorCidade = models.BooleanField()
    indicadorConcursoEspecial = models.IntegerField()
    listaDezenas = models.ArrayField(models.CharField(max_length=2))
    listaDezenasSegundoSorteio = models.ArrayField(models.CharField(max_length=2), null=True, blank=True)
    listaMunicipioUFGanhadores = models.ArrayField(models.CharField(max_length=50), null=True, blank=True)
    listaRateioPremio = models.ArrayField(models.EmbeddedModelField('RateioPremio'))
    localSorteio = models.CharField(max_length=50)
    nomeMunicipioUFSorteio = models.CharField(max_length=50)
    nomeTimeCoracaoMesSorte = models.CharField(max_length=50, null=True, blank=True)
    numero = models.IntegerField()
    numeroConcursoAnterior = models.IntegerField()
    numeroConcursoFinal_0_5 = models.IntegerField()
    numeroConcursoProximo = models.IntegerField()
    numeroJogo = models.IntegerField()
    observacao = models.TextField(null=True, blank=True)
    premiacaoContingencia = models.TextField(null=True, blank=True)
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

    class Meta:
        abstract = True


class RateioPremio(models.Model):
    descricaoFaixa = models.CharField(max_length=50)
    faixa = models.IntegerField()
    numeroDeGanhadores = models.IntegerField()
    valorPremio = models.FloatField()

    class Meta:
        abstract = True
