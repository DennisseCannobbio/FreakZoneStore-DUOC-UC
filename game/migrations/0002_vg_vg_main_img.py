# Generated by Django 2.2.6 on 2019-11-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vg',
            name='vg_main_img',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
