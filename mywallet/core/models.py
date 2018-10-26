from django.contrib.auth.models import User
from django.db import models

class TipoInvestimento(models.Model):
	tipo = models.CharField(max_length=30,null=True,blank=True)
	def __str__(self):
		return self.tipo

	class Meta:
		verbose_name = "Tipo de Investimento"
		verbose_name_plural = "Tipos de Investimentos"
		ordering = ["tipo"]

class Moeda(models.Model):
	nome = models.CharField(max_length=25,null=True,blank=True)
	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Moeda"
		verbose_name_plural = "Moedas"
		ordering = ["nome"]

class Investimento(models.Model):
	nome = models.CharField(max_length=25,null=True,blank=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	id_tipoInvestimento = models.ForeignKey(TipoInvestimento, on_delete=models.CASCADE,null=True,blank=True)
	id_moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE,null=True,blank=True)
	capital = models.FloatField()
	criacao = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Investimento"
		verbose_name_plural = "Investimentos"
		ordering = ["nome"]

class TipoDespesa(models.Model):
	tipo = models.CharField(max_length=30)

	def __str__(self):
		return self.tipo

	class Meta:
		verbose_name = "Tipo de Depesa"
		verbose_name_plural = "Tipos de Despesas"
		ordering = ["tipo"]

class Despesa(models.Model):
	nome = models.CharField(max_length=25,null=True,blank=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	id_tipoDespesa = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE,null=True,blank=True)
	id_moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE,null=True,blank=True)
	custo = models.FloatField(null=True,blank=True)
	criacao = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)

	def __str__(self):
		return self.nome
	
	class Meta:
		verbose_name = "Despesa"
		verbose_name_plural = "Despesas"
		ordering = ["nome"]
	
class Meta(models.Model):
	nome = models.CharField(max_length=25,null=True,blank=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	investimento = models.FloatField()
	despesa = models.FloatField()
	criacao = models.DateField(auto_now=False, auto_now_add=False)
	inicio = models.DateField(auto_now=False, auto_now_add=False)
	prazo  = models.DateField(auto_now=False, auto_now_add=False)
	descricao = models.CharField(max_length=200)

	def __str__(self):
		return self.nome
	
	class Meta:
		verbose_name = "Meta"
		verbose_name_plural = "Metas"
		ordering = ["nome"]
	
class Fundo(models.Model):
	nome = models.CharField(max_length=25,null=True,blank=True)
	id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	id_investimento = models.ForeignKey(Investimento, on_delete=models.CASCADE)
	id_despesa = models.ForeignKey(Despesa, on_delete=models.CASCADE)
	saldo = models.FloatField()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Fundo"
		verbose_name_plural = "Fundos"
		ordering = ["nome"]
