# Generated by Django 4.2.1 on 2023-06-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acervo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('sigla', models.CharField(max_length=30, unique=True)),
                ('descricao', models.TextField()),
                ('info_adicionais', models.TextField(blank=True, null=True)),
                ('ordem_exibicao', models.PositiveSmallIntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Acervos',
                'db_table': 'acervo',
                'ordering': ['ordem_exibicao'],
            },
        ),
    ]
