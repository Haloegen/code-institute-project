from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Category, Expense
from .forms import formExpenses
import json

from .forms import formExpenses
# Create your views here.

@login_required
def project_list(request):
    # Retrieves all projects from the database and renders them in the 'project-list.html' template
    project_list = Project.objects.all()
    return render(request, 'budget/project-list.html', {'project_list': project_list})

def project_detail(request, project_slug):
    # Retrieves details of a specific project and associated categories and expenses
    project = get_object_or_404(Project, slug=project_slug)

    if request.method == 'GET':
        # Fetches category list and renders project details in the 'project-detail.html' template
        category_list = Category.objects.filter(project=project)
        return render(request, 'budget/project-detail.html', {'project': project, 'expense_list':project.expenses.all(), 'category_list': category_list})

    elif request.method == 'POST' and project.author == request.user:
        # Handles expense creation for the project if the request method is POST and user is the project author
        form = formExpenses(request.POST)
        if form.is_valid():
            # Retrieves form data, creates an Expense object, and saves it to the database
            title = form.cleaned_data['title']
            cost = form.cleaned_data['cost']
            category_name = form.cleaned_data['category']
            category = get_object_or_404(Category, project=project, name=category_name)

            Expense.objects.create(
                project=project,
                title=title,
                cost=cost,
                category=category
            ).save()

    elif request.method == 'DELETE' and project.author == request.user:
        # Handles expense deletion if the request method is DELETE and user is the project author
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        return HttpResponse('')

    # Redirects to the project_slug URL
    return HttpResponseRedirect(project_slug)

class ProjectCreateView(CreateView):
    # Creates a new project using Django's CreateView, including handling category creation
    model = Project
    template_name = 'budget/add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Overrides form_valid method to create project and associated categories
        self.object = form.save(commit=False)
        self.object.save()
        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category,
            ).save()
            messages.add_message(self.request, messages.SUCCESS, 'Project Created')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        # Returns the success URL, which is the slugified project name
        return slugify(self.request.POST['name'])



@login_required
def delete_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    if project.author == request.user:
        project.delete()
        messages.success(request, "Project successfully deleted.")
    else:
        messages.error(request, "You do not have permission to delete this project.")
    return redirect('home')