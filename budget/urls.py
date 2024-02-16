from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name = 'home'),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('delete/<slug:project_slug>/', views.delete_project, name='delete_project'),
    path('<slug:project_slug>', views.project_detail, name = 'detail'),
]