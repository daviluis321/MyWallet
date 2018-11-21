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

def delete_page(request):
    return render(request, 'excluir_usuario.html')

def delete(request, username):
    
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.sucess(request, "Usuário excluído")
        return redirect('/home')
    except User.DoesNotExist:
       messages.error(request, "Usuario nao encontrado")
       return redirect('/home')
    except Exception as e:
        return render(request, 'index.html',{'err':"Erro"})
    return redirect('/home')