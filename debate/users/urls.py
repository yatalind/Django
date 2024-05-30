from django.urls import path
from .views import register
from .views import register, user_login, profil
from .views import not_ekle, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('giris/', user_login, name='giris'),
    path('profil/', profil, name='users-profil'),
    path('not-ekle/', not_ekle, name='not_ekle'),
    path('logout/', user_logout, name='logout'),
]