from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contato(request):
    return render(request, 'contato.html')

#@login_required
#def main(request):
    #return render(request, 'main.html')

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'main.html' 

def investimento(request):
    return render(request, 'investimento.html')

def despesa(request):
    return render(request, 'despesa.html')

def qsomos(request):
    return  render (request, 'qsomos.html')

index = IndexView.as_view()