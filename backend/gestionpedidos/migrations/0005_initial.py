# Generated by Django 4.1.1 on 2022-10-17 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("gestionpedidos", "0004_delete_persona"),
    ]

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("contrasena", models.CharField(max_length=100)),
                ("rol", models.CharField(default="repartidor", max_length=100)),
                ("tipoContrato", models.CharField(max_length=100)),
                ("estadoLaboral", models.CharField(max_length=100)),
                ("Rut", models.CharField(default="0", max_length=100, unique=True)),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="IngresarVenta",
            fields=[
                (
                    "idVenta",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("fechaVenta", models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="InventarioRecarga",
            fields=[
                (
                    "idProducto",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("NombreProducto", models.CharField(default="gas", max_length=100)),
                ("stock", models.IntegerField(default="0")),
                ("precio", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="InventarioVehiculo",
            fields=[
                (
                    "patente",
                    models.CharField(
                        max_length=8, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("fechaTecnica", models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "idPedido",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("direccion", models.CharField(max_length=100)),
                ("comentario", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="VehiculoOperativos",
            fields=[
                (
                    "IdVehiculo",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "idEmpleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.empleado",
                    ),
                ),
                (
                    "patente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.inventariovehiculo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recarga",
            fields=[
                (
                    "idRecarga",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("fechaRecarga", models.DateField(blank=True)),
                (
                    "IdVehiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.vehiculooperativos",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PedidoActivo",
            fields=[
                (
                    "idPedidoActivo",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "idPatente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.vehiculooperativos",
                    ),
                ),
                (
                    "idPedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.pedido",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pago",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipoPago", models.CharField(max_length=100)),
                (
                    "idVenta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.ingresarventa",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ingresarventa",
            name="idVehiculo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="gestionpedidos.vehiculooperativos",
            ),
        ),
        migrations.CreateModel(
            name="DetalleVenta",
            fields=[
                (
                    "idDetalleVenta",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("cantidadVenta", models.IntegerField()),
                ("subtotal", models.IntegerField()),
                (
                    "idProductos",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.inventariorecarga",
                    ),
                ),
                (
                    "idVenta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.ingresarventa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DetalleRecarga",
            fields=[
                (
                    "idDetalleRecarga",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("cantidad", models.IntegerField()),
                (
                    "idProductos",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.inventariorecarga",
                    ),
                ),
                (
                    "idRecarga",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestionpedidos.recarga",
                    ),
                ),
            ],
        ),
    ]
