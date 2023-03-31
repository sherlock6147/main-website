from django.urls import path
from base.views import *

app_name = 'base'
urlpatterns = [
    path('', home,name='home'),
    path('login/',redirect_to_google_login,name="redirect_to_google_login")
]