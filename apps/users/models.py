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
    
    

class Item(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class AreaDeServico(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Banheiro(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Quarto(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Cozinha(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Outros(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    


class Area(models.Model):
    nome = models.CharField(max_length=100)

class Item2(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)



