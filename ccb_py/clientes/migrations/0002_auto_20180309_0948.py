# Generated by Django 2.0.2 on 2018-03-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=60, null=True, verbose_name='email'),
        ),
    ]
