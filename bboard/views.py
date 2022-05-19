from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *


def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'bboard/index.html', context)

