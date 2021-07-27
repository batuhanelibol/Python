from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Takim

# Create your views here.

def index(request):
    teams = Takim.objects.all()

    context = {
        'teams': teams
    }
    return render(request, 'takim/list.html', context)

def detail(request, takim_id):
    team = get_object_or_404(Takim, pk= takim_id)
    context = {
        'team':team
    }
    return render(request, 'takim/detail.html', context)

def search(request):
    return render(request, 'takim/search.html')
