from django.db import models

# Create your models here.

class Usuario(models.Model):
	nome  = models.CharField(max_length=200)
	cpf   = models.CharField(max_length=11, unique=true)
	email = models.EmailField(max_length=80, unique=true)

class Investimento(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.cascade)
	capital    = models.FloatField()
	tipo	   = models.CharField(max_length=30)
	criacao    = models.DateField(auto_now=False, auto_now_add=False)
	modeda     = models.CharField(max_length=10)

class Despesa(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.cascade)
	custo      = models.FloatField()
	tipo	   = models.CharField(max_length=30)
	criacao    = models.DateField(auto_now=False, auto_now_add=False)
	modeda     = models.CharField(max_length=10)

class Meta(models.Model):
	id_usuario   = models.ForeignKey(Usuario, on_delete=models.cascade)
	investimento = models.FloatField()
	despesa      = models.FloatField()
	criacao		 = models.DateField(auto_now=False, auto_now_add=False)
	inicio		 = models.DateField(auto_now=False, auto_now_add=False)
	prazo		 = models.DateField(auto_now=False, auto_now_add=False)
	descricao	 = models.CharField(max_length=200)

class Fundo(models.Model):
	id_usuario   	= models.ForeignKey(Usuario, on_delete=models.cascade)
	id_investimento = models.ForeignKey(Investimento, on_delete=models.cascade)
	id_despesa   	= models.ForeignKey(Despesa, on_delete=models.cascade)
	saldo			= models.FloatField()

class GraficoMeta(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.cascade)
	id_meta    = models.ForeignKey(Meta, on_delete=models.cascade)
	criacao	   = models.DateField(auto_now=False, auto_now_add=False)

class GraficoFundo(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.cascade)
	id_fundo   = models.ForeignKey(Fundo, on_delete=models.cascade)
	criacao	   = models.DateField(auto_now=False, auto_now_add=False)