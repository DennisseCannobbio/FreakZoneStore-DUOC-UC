# Generated by Django 2.2.6 on 2019-11-28 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='cuent_ape',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='cuent_email',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='cuent_nombre',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='cuent_pass',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='user',
            field=models.OneToOneField(default=192827333, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='com_nombre',
            field=models.CharField(default=None, help_text='Ingrese el nombre de su comuna', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='cuent_fecnac',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='desp_direccion',
            field=models.TextField(default=None, help_text='Ingrese su dirección', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='desp_telef',
            field=models.CharField(default=None, help_text='Ingrese su número de teléfono', max_length=10, null=True),
        ),
    ]
