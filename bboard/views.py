from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


def index(request):
    boards = Board.objects.all()
    rubrics = Rubric.objects.all()
    context = {'boards': boards, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    boards = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'boards': boards, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BoardCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BoardForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context
