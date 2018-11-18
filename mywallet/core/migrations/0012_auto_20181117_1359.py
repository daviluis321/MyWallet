# Generated by Django 2.1.2 on 2018-11-17 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_fundo_nome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='despesa',
            options={'ordering': ['nome'], 'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
        migrations.AlterModelOptions(
            name='fundo',
            options={'ordering': ['nome'], 'verbose_name': 'Fundo', 'verbose_name_plural': 'Fundos'},
        ),
        migrations.AlterModelOptions(
            name='investimento',
            options={'ordering': ['nome'], 'verbose_name': 'Investimento', 'verbose_name_plural': 'Investimentos'},
        ),
        migrations.AlterModelOptions(
            name='meta',
            options={'ordering': ['nome'], 'verbose_name': 'Meta', 'verbose_name_plural': 'Metas'},
        ),
        migrations.AlterModelOptions(
            name='moeda',
            options={'ordering': ['nome'], 'verbose_name': 'Moeda', 'verbose_name_plural': 'Moedas'},
        ),
        migrations.AlterModelOptions(
            name='tipodespesa',
            options={'ordering': ['tipo'], 'verbose_name': 'Tipo de Depesa', 'verbose_name_plural': 'Tipos de Despesas'},
        ),
        migrations.AlterModelOptions(
            name='tipoinvestimento',
            options={'ordering': ['tipo'], 'verbose_name': 'Tipo de Investimento', 'verbose_name_plural': 'Tipos de Investimentos'},
        ),
    ]
