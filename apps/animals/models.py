from django.db import models

# Create your models here.

# Las clase se utiliza PascalCase
class Animal(models.Model):
    # Los nombres de las varibles se utiliza snake_case
    nombre = models.CharField(max_length=20, null=False, blank=False)
    edad = models.IntegerField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen = models.ImageField(upload_to='animals', null=False, blank=False)
    
    class Meta:
        db_table='animales'
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        ordering = ['-id']
        
    def __str__(self):
        return self.nombre + str(self.edad)