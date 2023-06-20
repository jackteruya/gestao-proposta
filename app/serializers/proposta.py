from rest_framework import serializers

from app.models import Proposta


class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = ['id', 'nome', 'cpf', 'endereco', 'valor']
        read_only_fields = ['id', ]
