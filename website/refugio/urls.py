from django.urls import path
from django.views.generic import TemplateView

from refugio.views.index import index
from refugio.views.login import login

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
]
