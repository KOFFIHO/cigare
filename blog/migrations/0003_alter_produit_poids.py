# Generated by Django 5.0.2 on 2024-02-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_produit_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='poids',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]