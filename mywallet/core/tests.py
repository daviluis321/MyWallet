from django.core.urlresolvers import reverse
from django.test import TestCase


from django.test import TestCase
from .views import home
from .views import login
from .views import contato
from .views import main
from .views import investimento
from .views import despesa
from .views import qsomos

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
            view = resolve('/')
            self.assertEquals(view.func, home)

    def test_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
   	def test_main_view_status_code(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contato_view_status_code(self):
        url = reverse('contato')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_quem_somos_view_status_code(self):
        url = reverse('quem_somos')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class LoginTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/login')
            self.assertEquals(view.func, login)

class RecuperaSenhaTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/recuperaSenha')
            self.assertEquals(view.func, recuperaSenha)

class ContatoTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/contato')
            self.assertEquals(view.func, contato)

class MainTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/main')
            self.assertEquals(view.func, main)

class InvestimentoTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/investimento')
            self.assertEquals(view.func, investimento)

class DespesaTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/despesa')
            self.assertEquals(view.func, despesa)

class QSOMOSTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/qsomos')
            self.assertEquals(view.func, qsomos)
