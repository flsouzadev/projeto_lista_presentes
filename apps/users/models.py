from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Convidado(models.Model):
    
    nome = models.CharField(max_length=100, null=True, blank=False)
    rg = models.CharField(max_length=20, unique=True)
    presente = models.CharField(max_length=5, null=True, blank=False)
    presenca = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    

class AreaDeServico(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class Banheiro(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class Quarto(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class Cozinha(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class Outros(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item




