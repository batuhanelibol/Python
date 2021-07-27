# Generated by Django 3.2.3 on 2021-06-02 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kayitlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Adı Soyadı')),
                ('tc', models.CharField(max_length=11, verbose_name='TC Kimlik No')),
                ('telno', models.CharField(max_length=11, verbose_name='Telefon Numarası')),
                ('isgecmisi', models.TextField(verbose_name='Daha önce çalıştığınız yerler')),
                ('iskazaları', models.TextField(verbose_name='Geçirmiş olduğunuz iş kazaları')),
                ('engel', models.TextField(verbose_name='Engeliniz')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
        ),
        migrations.DeleteModel(
            name='Calisanlar',
        ),
    ]
