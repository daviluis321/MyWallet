"""mywallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/',accounts_views.cadastro,name='cadastro'),
    path('contato/',views.contato, name='contato'),
    path('admin/', admin.site.urls),
    path('main/',views.main, name='main'),
    path('investimento/',views.investimento, name='investimento'),
    path('despesa/',views.despesa, name='despesa'),
    path('qsomos/',views.qsomos, name = 'qsomos'),
    path('delete/', accounts_views.delete, name='del_user')
]
