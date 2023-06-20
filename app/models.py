from django.db import models


class StatusProposta(models.TextChoices):
    EM_ANALISE = 'Em analise'
    NEGADO = 'Negado'
    APROVADO = 'Aprovado'


class Proposta(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=128)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.CharField(
        max_length=32,
        choices=StatusProposta.choices,
        default=StatusProposta.EM_ANALISE,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome} - {self.cpf}'
