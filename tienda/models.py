from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('categoria-list')
    def __str__(self):
    	return self.nombre


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    def __str__(self):
    	return self.nombre
    
    
    