from django.urls import reverse, resolve
from django.test import TestCase, Client
from core.views import home,contato, main, investimento, despesa, qsomos
from accounts.views import cadastro
from django.contrib.auth import views as auth_views

class CoreReturnUrl(TestCase):
    def setUp(self):
        self.client = Client()
        self.login = reverse('login')

    def test_url_home(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
   
    def test__url_login(self):
        response = self.client.get(self.login)
        self.assertTemplateUsed(response, 'login.html')

    def test__url_cadastro(self):
        view = resolve('/cadastro/')
        self.assertEquals(view.func, cadastro )
    
    def test__url_contato(self):
        view = resolve('/contato/')
        self.assertEquals(view.func, contato)

    def test__url_main(self):
        view = resolve('/main/')
        self.assertEquals(view.func, main)

    def test__url_investimento(self):
        view = resolve('/investimento/')
        self.assertEquals(view.func, investimento)
    
    def test__url_despesa(self):
        view = resolve('/despesa/')
        self.assertEquals(view.func, despesa)

    def test__url_qsomos(self):
        view = resolve('/qsomos/')
        self.assertEquals(view.func, qsomos)