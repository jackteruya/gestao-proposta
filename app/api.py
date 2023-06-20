from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.models import Proposta
from app.serializers.proposta import PropostaSerializer
from .services import PropostaService

from .tasks import avaliar_proposta


class PropostaAPIViewSet(CreateAPIView):
    serializer_class = PropostaSerializer
    queryset = Proposta.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PropostaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data['id']
            avaliar_proposta.delay(id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
