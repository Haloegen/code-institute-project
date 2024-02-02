from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_budget(request):
    return HttpResponse("I have tested this")

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    return render(request, 'budget/project-detail.html')