# Generated by Django 2.2.7 on 2021-06-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20210620_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='duvidas',
            name='Tipo_de_duvida',
            field=models.CharField(choices=[('PYT', 'Python'), ('DJA', 'Django'), ('HTM', 'HTML'), ('CSS', 'css')], default='PYT', max_length=3),
        ),
        migrations.AddField(
            model_name='duvidas',
            name='dificuldade',
            field=models.CharField(choices=[('DIF', 'Difícil'), ('MED', 'Médio'), ('SIM', 'Simples')], default='DIF', max_length=3),
        ),
    ]
