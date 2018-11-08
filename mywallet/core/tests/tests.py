from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
import datetime
from core.models import Investimento, TipoInvestimento, Moeda, Meta, Despesa, Fundo, TipoDespesa, Fundo

from django.test import TestCase
from core.views import home, login, contato, main, investimento, despesa, qsomos

#testes Brena
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
