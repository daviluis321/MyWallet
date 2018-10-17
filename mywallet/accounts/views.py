from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def cadastro(request):
    form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})