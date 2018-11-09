from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
import datetime
#export DJANGO_SETTINGS_MODULE=core.settings.__init__
from core.models import Investimento, TipoInvestimento, Moeda, Meta, Despesa, Fundo, TipoDespesa, Fundo

class BancoTestsTamanho(TestCase):
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
    def testeTmoeda(self):
        self.assertEquals(Moeda.objects.count(),1)
    def testeTtipoinvestimento(self):
        self.assertEquals(TipoInvestimento.objects.count(),1)
    def testeTinvestimento(self):    
        self.assertEquals(Investimento.objects.count(),1)
    def testeTmeta(self):    
        self.assertEquals(Meta.objects.count(),1)
