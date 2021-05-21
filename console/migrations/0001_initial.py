# Generated by Django 2.2.6 on 2019-11-16 22:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conectividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_conectividad', models.CharField(help_text='Tipo conectividad de la consola', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('con_id', models.CharField(help_text='Id de la consola', max_length=10, primary_key='True', serialize=False)),
                ('con_nom', models.CharField(help_text='Nombre de la consola', max_length=100)),
                ('con_peso', models.IntegerField(help_text='Peso de la consola')),
                ('con_descr', models.TextField(help_text='Ingrese la descripción de la consola', max_length=3000, null=True)),
                ('con_precio', models.IntegerField(help_text='Precio de la consola')),
                ('con_resolucion', models.CharField(help_text='Resolucion de la consola', max_length=50)),
                ('con_color', models.CharField(help_text='Color de la consola', max_length=20)),
                ('con_autonomia', models.CharField(help_text='Duracion de la Bateria', max_length=20)),
                ('con_memoria', models.CharField(help_text='Memoria interna de la consola', max_length=20)),
                ('con_main_img', models.ImageField(null=True, upload_to='gallery')),
                ('con_conectividad', models.ManyToManyField(to='console.Conectividad')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_tipo', models.CharField(help_text='Tipo de la consola', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ConsolaInstance',
            fields=[
                ('inst_id', models.UUIDField(default=uuid.uuid4, help_text='ID para esta unidad', primary_key=True, serialize=False)),
                ('inst_on_stock', models.BooleanField(null=True)),
                ('inst_consola', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='console.Consola')),
            ],
            options={
                'ordering': ['inst_id'],
            },
        ),
        migrations.AddField(
            model_name='consola',
            name='con_tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='console.Tipo'),
        ),
    ]
