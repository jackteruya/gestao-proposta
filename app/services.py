from time import sleep

from app.models import StatusProposta


class PropostaService:

    def __init__(self, model):
        self.model = model

    def validar(self, id: int):
        sleep(5)
        proposta = self.model.objects.get(id=id)
        ultima_proposta_avaliada = (
            self.model.objects.exclude(status=StatusProposta.EM_ANALISE)
            .exclude(id=proposta.id)
            .last()
        )

        if ultima_proposta_avaliada is None or ultima_proposta_avaliada.status == StatusProposta.NEGADO:
            proposta.status = StatusProposta.APROVADO
        else:
            proposta.status = StatusProposta.NEGADO
        proposta.save(update_fields=['status'])