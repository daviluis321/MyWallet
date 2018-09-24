from django.db import models

# Create your models here.

class Usuario(models.Model):
	nome  = models.CharField(max_length=200)
	cpf   = models.CharField(max_length=11, unique=True)
	email = models.EmailField(max_length=80, unique=True)

class TipoInvestimento(models.Model):
	tipo = models.CharField(max_length=30)

class Moeda(models.Model):
	nome = models.CharField(max_length=10)

class Investimento(models.Model):
	id_usuario 			= models.ForeignKey(Usuario, on_delete=models.CASCADE)
	id_tipoInvestimento = models.ForeignKey(TipoInvestimento, on_delete=models.CASCADE)
	id_moeda			= models.ForeignKey(Moeda, on_delete=models.CASCADE)
	capital    			= models.FloatField()
	criacao    			= models.DateField(auto_now=False, auto_now_add=False)

class TipoDespesa(models.Model):
	tipo = models.CharField(max_length=30)

class Despesa(models.Model):
	id_usuario	   = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	id_tipoDespesa = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE)
	id_moeda	   = models.ForeignKey(Moeda, on_delete=models.CASCADE)
	custo     	   = models.FloatField()
	criacao    	   = models.DateField(auto_now=False, auto_now_add=False)



class Meta(models.Model):
	id_usuario   = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	investimento = models.FloatField()
	despesa      = models.FloatField()
	criacao		 = models.DateField(auto_now=False, auto_now_add=False)
	inicio		 = models.DateField(auto_now=False, auto_now_add=False)
	prazo		 = models.DateField(auto_now=False, auto_now_add=False)
	descricao	 = models.CharField(max_length=200)

class Fundo(models.Model):
	id_usuario   	= models.ForeignKey(Usuario, unique=True, on_delete=models.CASCADE)
	id_investimento = models.ForeignKey(Investimento, on_delete=models.CASCADE)
	id_despesa   	= models.ForeignKey(Despesa, on_delete=models.CASCADE)
	saldo			= models.FloatField()
