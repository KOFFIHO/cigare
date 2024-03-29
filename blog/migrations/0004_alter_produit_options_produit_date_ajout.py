# Generated by Django 5.0.2 on 2024-02-19 15:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_produit_poids'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ['-date_ajout']},
        ),
        migrations.AddField(
            model_name='produit',
            name='date_ajout',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
