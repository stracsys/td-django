# Generated by Django 4.0.1 on 2022-02-07 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='magasin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_magasin', to='polls.magasin'),
        ),
    ]
