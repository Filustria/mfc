# Generated by Django 2.2.7 on 2021-06-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duvidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duvida', models.CharField(max_length=50)),
                ('Descricao', models.CharField(max_length=500)),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Duvida',
                'verbose_name_plural': 'Duvidas',
            },
        ),
        migrations.AlterModelOptions(
            name='membros',
            options={'verbose_name': 'Membro', 'verbose_name_plural': 'Membros'},
        ),
    ]
