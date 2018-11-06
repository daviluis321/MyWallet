from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
import datetime
from .models import Investimento, TipoInvestimento, Moeda, Meta, Despesa, Fundo, TipoDespesa, Fundo

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
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

   # def test_home_url_resolves_home_view(self):
    #        view = resolve('/')
    #        self.assertEquals(view.func, home)

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
        url = reverse('qsomos')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
class BancoTests(TestCase):
    def setUp(self):
        self.usuario, novo = User.objects.get_or_create(username='admin')
        self.tipo_investimento, novo = TipoInvestimento.objects.get_or_create(tipo='tipo')
        self.tipo_despesa, novo = TipoDespesa.objects.get_or_create(tipo='tipo')
        self.moeda, novo = Moeda.objects.get_or_create(nome='real')
        self.investimento = Investimento.objects.get_or_create(id_usuario=self.usuario,id_tipoInvestimento=self.tipo_investimento,id_moeda=self.moeda,capital=100.30,criacao=datetime.date(2010, 1, 1))                
        self.investimento2 = Investimento.objects.get_or_create(id_usuario=self.usuario,id_tipoInvestimento=self.tipo_investimento,id_moeda=self.moeda,capital=100.30,criacao=datetime.date(2010, 1, 1))
        #self.despesa = Despesa.objects.get_or_create(id_usuario=self.usuario, id_tipoDespesa=self.tipo_despesa,id_moeda=self.moeda, custo=200.22, criacao=datetime.date(2010,1,1))
        self.meta = Meta.objects.get_or_create(id_usuario=self.usuario, investimento=200.00,despesa=50.23,criacao=datetime.date(2010, 1, 1),inicio=datetime.date(2010, 2, 2),prazo=datetime.date(2010, 3, 3),descricao='Arrozzzzz')
        #self.fundo = Fundo.objects.get_or_create(id_usuario=self.usuario,id_investimento=self.id_investimento,id_despesa=self.despesa,,saldo=4000.12)      
        #self.investimento = Investimento.objects.get_or_create(id_usuario=self.usuario,id_tipoInvestimento=self.tipo_investimento,id_moeda=self.moeda,capital=100.30,criacao=datetime.date(2010, 1, 1))
        print('fdsfsd',self.usuario)
    def tearDown(self):
        pass
    def testes(self):
        self.assertEquals(1+1,2)
        self.assertEquals(Moeda.objects.count(),1)
        self.assertEquals(TipoInvestimento.objects.count(),1)
        self.assertEquals(Investimento.objects.count(),1)
        self.assertEquals(Meta.objects.count(),1)


