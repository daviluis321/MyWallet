from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form =SignUpForm()
    return render(request, 'cadastro.html', {'form': form})


def delete(request, username = "xcarol"):
    
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.sucess(request, "Usuário excluído")
    except User.DoesNotExist:
       messages.error(request, "Usuario nao encontrado")
       return redirect('home')
    except Exception as e:
        return render(request, 'index.html',{'err':"Erro"})
    return redirect('qsomos')