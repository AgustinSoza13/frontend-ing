# Generated by Django 4.1.1 on 2022-12-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestionpedidos", "0017_alter_ingresarventa_idventa"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingresarventa",
            name="fechaVentita",
            field=models.DateField(null=True),
        ),
    ]