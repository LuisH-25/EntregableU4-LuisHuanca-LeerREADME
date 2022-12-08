from django.db import models

# Create your models here.

class Portafolio(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    tag = models.CharField(max_length=20)
    url = models.CharField(max_length=80)

    def __str__(self):
        return self.titulo + " - " + self.url

    class Meta:
        db_table = "portafolios"