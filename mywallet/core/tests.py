from django.test import TestCase
from .views import home
from .views import login
from .views import contato
from .views import main
from .views import investimento
from .views import despesa
from .views import qsomos

# Create your tests here.

class HomeTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/')
            self.assertEquals(view.func, home)

class LoginTests(TestCase):
    def test_home_url_resolves_home_view(self):
            view = resolve('/login')
            self.assertEquals(view.func, login)

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
