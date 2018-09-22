from django.db import models

# Create your models here.

class Usuario(models.Model):
	nome  = models.CharField(max_length=200)
	cpf   = models.CharField(max_length=11, unique=True)
	email = models.EmailField(max_length=80, unique=True)

class Investimento(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	capital    = models.FloatField()
	tipo	   = models.CharField(max_length=30)
	criacao    = models.DateField(auto_now=False, auto_now_add=False)
	modeda     = models.CharField(max_length=10)

class Despesa(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	custo      = models.FloatField()
	tipo	   = models.CharField(max_length=30)
	criacao    = models.DateField(auto_now=False, auto_now_add=False)
	modeda     = models.CharField(max_length=10)

class Meta(models.Model):
	id_usuario   = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	investimento = models.FloatField()
	despesa      = models.FloatField()
	criacao		 = models.DateField(auto_now=False, auto_now_add=False)
	inicio		 = models.DateField(auto_now=False, auto_now_add=False)
	prazo		 = models.DateField(auto_now=False, auto_now_add=False)
	descricao	 = models.CharField(max_length=200)

class Fundo(models.Model):
	id_usuario   	= models.ForeignKey(Usuario, on_delete=models.CASCADE)
	id_investimento = models.ForeignKey(Investimento, on_delete=models.CASCADE)
	id_despesa   	= models.ForeignKey(Despesa, on_delete=models.CASCADE)
	saldo			= models.FloatField()

class GraficoMeta(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	id_meta    = models.ForeignKey(Meta, on_delete=models.CASCADE)
	criacao	   = models.DateField(auto_now=False, auto_now_add=False)

class GraficoFundo(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	id_fundo   = models.ForeignKey(Fundo, on_delete=models.CASCADE)
	criacao	   = models.DateField(auto_now=False, auto_now_add=False)