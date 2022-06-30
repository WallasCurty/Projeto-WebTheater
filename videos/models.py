from django.db import models

# Create your models here.
class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    qtd_vizu = models.IntegerField()
    video = models.URLField()
    imagem = models.URLField()

class Categoria(models.Model):
    titulo_cat = models.CharField(max_length=100)
    descricao_cat = models.TextField()
    imagem_cat = models.URLField()

