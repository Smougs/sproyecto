# Generated by Django 4.0.5 on 2022-06-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prestamo', '0005_remove_prestamo_entregado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
