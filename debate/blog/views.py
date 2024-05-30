from django.shortcuts import render
from .models import Egitim, Haber

def home(request):
    return render(request, 'blog/home.html')

def haberler(request):
    haberler = Haber.objects.all()
    context = {
        'haberler': haberler,
    }
    return render(request, 'blog/haberler.html', context)

def egitimler(request):
    # Egitimler tablosundaki tüm öğeleri alın
    egitimler = Egitim.objects.all()

    context = {
        'egitimler': egitimler,  # Şablona aktarılacak veri
    }

    return render(request, 'blog/egitimler.html', context)

def profilim(request):
    return render(request, 'blog/profilim.html')



# Create your views here.
