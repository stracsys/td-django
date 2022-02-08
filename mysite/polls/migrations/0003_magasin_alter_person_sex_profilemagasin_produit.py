# Generated by Django 4.0.1 on 2022-01-27 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_person_age_person_country_person_name_person_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA-FASO'), ('CI', "COTE D'IVOIRE"), ('SN', 'SENEGAL')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('MASCULIN', 'MASCULIN'), ('FEMININ', 'FEMININ-FASO'), ('NON-DEFINI', 'NON-DEFINI')], max_length=10),
        ),
        migrations.CreateModel(
            name='ProfileMagasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Magasin address mail')),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('magasin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='magasin_profile', to='polls.magasin')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA-FASO'), ('CI', "COTE D'IVOIRE"), ('SN', 'SENEGAL')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='PRODUCT_IMG')),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_magasin', to='polls.magasin')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]