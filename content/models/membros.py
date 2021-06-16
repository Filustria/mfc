from django.db import models

class Membros(models.Model):
    nome = models.CharField(max_length=255)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.nome} - {self.id}"

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"