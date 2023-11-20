from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Requisito(models.Model):
    temperatura = models.DecimalField(max_digits=3, decimal_places=1, help_text='Temperatura ideal en grados celsius')
    humedad = models.DecimalField(max_digits=3, decimal_places=1, help_text='Valor para el porcentaje de humedad')
    ph_suelo = models.DecimalField(max_digits=3, decimal_places=1, help_text='PH ideal del suelo. Rango: 0 a 14',
                                   validators=[MinValueValidator(0), MaxValueValidator(14)])
    cantidad_riego = models.DecimalField(max_digits=3, decimal_places=1, help_text='Riego en litros')
    nota_complementaria = models.TextField(null=True)

    class Meta:
        db_table = 'requisitos'


class Cuidado(models.Model):
    ESTADOS_CRECIMIENTO = [('Germinación', 'Germinación'), ('Crecimiento vegetativo', 'Crecimiento Vegetativo'), (
        'Fructificación', 'Fructificación'), ('Senescencia', 'Senescencia')]
    estado_crecimiento = models.CharField(max_length=50, choices=ESTADOS_CRECIMIENTO)
    descripcion = models.TextField()

    class Meta:
        db_table = 'cuidados'


class Cultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=100)
    TIPOS_ALIMENTO = [('Tubérculo', 'Tubérculo'), ('Fruta', 'Fruta'), ('Hortaliza', 'Hortaliza')]
    tipo_alimento = models.CharField(max_length=10, choices=TIPOS_ALIMENTO)
    TIPOS_PROPAGACION = [('Tallo', 'Tallo'), ('Semilla', 'Semilla')]
    tipo_propagacion = models.CharField(max_length=10, choices=TIPOS_PROPAGACION)

    class Meta:
        db_table = 'cultivos'


class ColeccionCultivo(models.Model):
    cultivo = models.OneToOneField(Cultivo, on_delete=models.CASCADE)
    requisito = models.OneToOneField(Requisito, null=True, on_delete=models.CASCADE)
    cuidado = models.ManyToManyField(Cuidado, related_name='cuidados')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'colecciones_cultivos'
