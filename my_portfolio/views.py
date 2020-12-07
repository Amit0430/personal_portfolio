from django.shortcuts import render
from .models import Project

def home(request):

    projects = Project.objects.order_by('-id')

    return render(request, 'my_portfolio_pages/home.html', {'projects':projects})
