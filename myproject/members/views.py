from django.shortcuts import render
from django.views.generic import ListView
from .models import Coaches
# Create your views here.

class CoachesList(ListView):
    template_name = 'members/coaches/coaches.html'
    queryset = Coaches.objects.all()
    context_object_name = 'coaches'

class TopAthleteList(ListView):
    template_name = 'members/top_athlete/top_athlete.html'
    queryset = Coaches.objects.all()
    context_object_name = 'athlete'