from django.db import models

# Create your models here.
class tienda(models.Model):
    direccion = models.CharField(max_length=50) 
    provincia = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    fechaCreacion = models.DateField(null=True, blank=True)
    telefonoContacto = models.CharField(max_length=9)

class producto(models.Model):
    descripcion = models.CharField(max_length=100)
    codigo = models.CharField(max_length=4)
    precioVenta = models.DecimalField(max_digits=5,decimal_places=2)
    cantidad = models.IntegerField(4)
    tiendaRelacionada = models.ForeignKey(tienda,blank=True,null=True,on_delete=models.SET_NULL)