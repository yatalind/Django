from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('admin/', admin.site.urls),
    path('haberler/', views.haberler, name='blog-haberler'),
    path('profilim/', views.profilim, name='blog-profilim'),
     path('egitimler/', views.egitimler, name='blog-egitimler'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)