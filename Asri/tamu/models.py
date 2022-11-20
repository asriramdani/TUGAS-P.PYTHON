from django.db import models


# Create your models here.
class Guest(models.Model):
    nim = models.CharField(max_length = 10)
    nama = models.CharField(max_length =250)
    kegiatan = models.TextField()
    def __str__(self):
        return self.nim