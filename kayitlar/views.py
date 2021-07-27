from django.shortcuts import render,redirect

# Create your views here.


def calisan(request):
    return render(request, 'kayitlar/calisan.html')
