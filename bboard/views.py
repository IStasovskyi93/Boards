from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *


def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    boards = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'boards': boards, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)
