# Generated by Django 2.2.7 on 2021-06-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20210622_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duvidas',
            name='Descricao',
            field=models.TextField(max_length=500),
        ),
    ]
