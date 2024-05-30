from django.db import models

class Egitim(models.Model):
    # Model alanları buraya eklenir
    baslik = models.CharField(max_length=100)
    icerik = models.TextField()
    tarih = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.baslik

class Haber(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    resim = models.ImageField(upload_to='haber_resimleri/', null=True, blank=True)

    def __str__(self):
        return self.baslik

# Create your models here.
