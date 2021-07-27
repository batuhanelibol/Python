from django.db import models

# Create your models here.



class Profil(models.Model):
    name = models.CharField(max_length=100, verbose_name='Adı Soyadı')
    tc = models.CharField(max_length=11, verbose_name='TC Kimlik No')
    telno = models.CharField(max_length=11, verbose_name='Telefon Numarası')
    isgecmisi = models.TextField(verbose_name='Daha önce çalıştığınız yerler')
    iskazaları = models.TextField(verbose_name='Geçirmiş olduğunuz iş kazaları')
    engel = models.TextField(verbose_name='Engeliniz')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')


    def __str__(self):
        return self.name
