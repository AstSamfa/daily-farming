# Generated by Django 4.2.6 on 2023-11-13 18:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_crecimiento', models.CharField(choices=[('Germinación', 'Germinación'), ('Crecimiento vegetativo', 'Crecimiento Vegetativo'), ('Fructificación', 'Fructificación'), ('Senescencia', 'Senescencia')], max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'cuidados',
            },
        ),
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cultivo', models.CharField(max_length=100)),
                ('tipo_alimento', models.CharField(choices=[('Tubérculo', 'Tubérculo'), ('Fruta', 'Fruta'), ('Hortaliza', 'Hortaliza')], max_length=10)),
                ('tipo_propagacion', models.CharField(choices=[('Tallo', 'Tallo'), ('Semilla', 'Semilla')], max_length=10)),
            ],
            options={
                'db_table': 'cultivos',
            },
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.DecimalField(decimal_places=1, help_text='Temperatura ideal en grados', max_digits=3)),
                ('humedad', models.DecimalField(decimal_places=1, help_text='Valor para el porcentaje de humedad', max_digits=3)),
                ('ph_suelo', models.DecimalField(decimal_places=1, help_text='PH ideal del suelo. Rango: 0 a 14', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(14)])),
                ('cantidad_riego', models.DecimalField(decimal_places=1, help_text='Riego en litros', max_digits=3)),
                ('nota_complementaria', models.TextField(null=True)),
            ],
            options={
                'db_table': 'requisitos',
            },
        ),
        migrations.CreateModel(
            name='ColeccionCultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuidado', models.ManyToManyField(related_name='cuidados', to='farm.cuidado')),
                ('cultivo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='farm.cultivo')),
                ('requisito', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='farm.requisito')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'colecciones_cultivos',
            },
        ),
    ]