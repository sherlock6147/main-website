from django.shortcuts import render,redirect
from projects.models import Project
from django.contrib.auth.models import AnonymousUser
from base.models import *
from projects.views import get_case_studies

# utilities
def prepare_context(request,access_level=1):
    context = {}
    if request.user.is_authenticated:
        is_whitelisted = len(WhiteListedPeople.objects.filter(user = request.user)) != 0
    else:
        is_whitelisted = False
    context['is_whitelisted'] = is_whitelisted
    # logging.debug(context)
    print(context)
    return context
# Create your views here.
def home(request):
    context = {}
    context = prepare_context(request)
    context['case_studies'] = get_case_studies()
    tech_tags = set()
    for study in get_case_studies():
        for tag in study.technologies_used.all():
            tech_tags.add(tag.name)
    context['tech_tags'] = tech_tags
    print(context)
    return render(request,'base/home.html',context)

def redirect_to_google_login(request):
    return redirect('/accounts/google/login')