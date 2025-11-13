from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    lugar = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='eventos', null=True, blank=True)
    
    def __str__(self):
        return self.titulo