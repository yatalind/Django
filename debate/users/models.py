from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Ekstra alanlar ekleyebilirsiniz
    pass

class Not(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    baslik = models.CharField(max_length=100)
    icerik = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

# Create your models here.
