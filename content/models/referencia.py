from django.db import models

class Referencia(models.Model):
    nome = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)
    revista = models.CharField(max_length=255)
    url = models.URLField(max_length=200)