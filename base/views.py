from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    context = {}
    return render(request,'base/home.html',context)

def redirect_to_google_login(request):
    return redirect('/accounts/google/login')