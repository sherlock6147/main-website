from django.shortcuts import render
from projects.models import *

# utilities
def get_published_projects():
    return Project.objects.filter(is_published=True).order_by('-order')

def get_unpublished_projects():
    return Project.objects.filter(is_published=False).order_by('-order')

def get_all_projects():
    return Project.objects.order_by('-order')

def get_case_studies():
    return Project.objects.filter(is_case_study=True).order_by('-order')
# Create your views here.