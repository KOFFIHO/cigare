# Generated by Django 5.0.2 on 2024-02-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='numero',
            field=models.CharField(max_length=10),
        ),
    ]
