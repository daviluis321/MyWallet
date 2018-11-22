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
from django.conf.urls import url, include

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/',accounts_views.cadastro,name='cadastro'),
    path('contato/',views.contato, name='contato'),
    path('admin/', admin.site.urls),
    path('main/',views.index, name='main'),
    path('investimento/',views.investimento, name='investimento'),
    path('despesa/',views.despesa, name='despesa'),
    path('qsomos/',views.qsomos, name = 'qsomos'),
    path('alterar_page/', accounts_views.alterar_page, name='alterar_page'),
    path('delete_page/', accounts_views.delete_page, name='delete_page'),
    path('delete/<username>', accounts_views.delete, name='delete'),
    url(r'password_reset/$',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    url(r'password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    url(r'^', include('django.contrib.auth.urls')),
]
