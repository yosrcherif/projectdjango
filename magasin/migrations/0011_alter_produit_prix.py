# Generated by Django 3.2 on 2021-04-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0010_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
