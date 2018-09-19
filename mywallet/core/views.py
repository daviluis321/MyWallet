from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contato(request):
    return render(request, 'contato.html')
