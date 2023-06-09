# Generated by Django 3.2 on 2023-06-04 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(choices=[('ING', 'Ingreso'), ('EGR', 'Egreso')], default='ING', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='ComprobanteProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.item')),
                ('comprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.comprobante')),
            ],
        ),
        migrations.AddField(
            model_name='comprobante',
            name='articulos',
            field=models.ManyToManyField(through='productos.ComprobanteProducto', to='productos.Item'),
        ),
    ]
