from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add_board/', BoardCreateView.as_view(), name='add_board')
]
