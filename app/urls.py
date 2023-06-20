from django.urls import path

from app.api import PropostaAPIViewSet
from app.views import index

urlpatterns = [
    path('', index),
    path('proposta/', PropostaAPIViewSet.as_view()),
]
