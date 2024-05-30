from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Not
from .models import CustomUser
from .forms import NotEkleForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Anasayfaya yönlendirme
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # Kullanıcı başarıyla giriş yaptı, yönlendirilecek sayfayı buraya yazabilirsiniz
            return redirect('http://127.0.0.1:8000/')  # Örnek olarak 'anasayfa' isimli bir URL'ye yönlendiriyoruz
        else:
            # Kullanıcı giriş bilgileri hatalı
            return render(request, 'users/giris.html', {'hata_mesaji': 'Kullanıcı adı veya şifre hatalı.'})
    else:
        return render(request, 'users/giris.html')
    
def profil(request):
    if isinstance(request.user, AnonymousUser):
        return redirect('giris')
    user = request.user
    notlar = Not.objects.filter(user=user)
    return render(request, 'users/profil.html', {'notlar': notlar})  

def not_ekle(request):
    if request.method == 'POST':
        form = NotEkleForm(request.POST)
        if form.is_valid():
            not_obj = form.save(commit=False)
            not_obj.user = request.user
            not_obj.save()
            return redirect('http://127.0.0.1:8000/users/profil/')  # veya not eklenen sayfaya yönlendirme
    else:
        form = NotEkleForm()
    return render(request, 'users/not_ekle.html', {'form': form})  

def user_logout(request):
    logout(request)
    return redirect('giris')
# Create your views here.
