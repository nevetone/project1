from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Nowosci(models.Model):
    tytul = models.CharField(max_length=60)
    opis = models.TextField()
    data = models.DateField()
    glowny = models.BooleanField()
    autor = models.CharField(max_length=20)
    CzyMaZdjecie = models.BooleanField()
    nazwaZdj = models.FileField(null=True , blank=True)
    
    class Meta:
        verbose_name_plural = "News"
        
    def __str__(self):
        return self.tytul
    