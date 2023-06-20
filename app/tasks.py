from celery import shared_task

from app.models import Proposta
from app.services import PropostaService


@shared_task
def avaliar_proposta(id):
    service = PropostaService(Proposta)
    service.validar(id)
