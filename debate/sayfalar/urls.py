from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('kayit/', views.kayit, name='kayit'),# Anasayfa için yönlendirme
    path('giris/', views.giris, name='giris'),
    path('cikis/', auth_views.LogoutView.as_view(), name='cikis'),
]