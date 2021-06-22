from django.db import models
from django.db.models.aggregates import Max
from django.core.validators import MaxValueValidator, MinValueValidator


tipo_de_duvida = [
        ('PYT', 'Python'), 
        ('DJA', 'Django'), 
        ('HTM', 'HTML'), 
        ('CSS', 'css'),
    ]


class Duvidas(models.Model):
    Duvida = models.CharField(max_length=50)
    Descricao = models.TextField(max_length=500)
    Date = models.DateTimeField(auto_now=True)
    Tipo_de_duvida = models.CharField(
        max_length=3,
        choices=tipo_de_duvida,
        default='PYT')
    novidade = models.BooleanField(verbose_name="Esta dúvida é nova para você?")
    dificuldade = models.PositiveIntegerField(verbose_name="Qual o grau de dificuldade desta dúvida?",
    validators=[MinValueValidator(1), MaxValueValidator(10)])



    def __str__(self):
        return f"{self.Duvida}"

    class Meta:
        verbose_name = "Duvida"
        verbose_name_plural = "Duvidas"