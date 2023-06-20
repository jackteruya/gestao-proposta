from django.http import HttpResponse
from django.shortcuts import render

# from app.tasks import make_add


def index(request):
    # make_add.delay()
    return render(request, template_name='index.html')
