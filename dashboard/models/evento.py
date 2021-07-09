from django.db import models

tipo_de_evento = (('EXAME','Exame laboratorial'), 
                ('DIAGN','Condições crônicas'), 
                ('FOLLO','Follow-up'), 
                ('REFS','Referência ao nível secundário'),
                ('HOSPT','Internação hospitalar'))

class Evento(models.Model):
    nome = models.CharField(max_length=250)
    tipo = models.CharField(
        max_length=5,
        choices=tipo_de_evento,
        default='EXAME')
    risco = models.FloatField()
    oportunidades = models.PositiveIntegerField()
    ocorrencias = models.PositiveIntegerField()
    ponto = models.FloatField(default=1)
    upper = models.FloatField(default=1)
    lower = models.FloatField(default=1)