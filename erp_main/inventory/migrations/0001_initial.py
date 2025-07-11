# Generated by Django 5.2.3 on 2025-06-19 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costing_method', models.CharField(choices=[('FIFO', 'FIFO'), ('LIFO', 'LIFO'), ('Weighted Average', 'Weighted Average')], max_length=50)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CycleCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_id', models.CharField(max_length=64)),
                ('success', models.BooleanField(default=False)),
                ('report_link', models.TextField(blank=True, null=True)),
                ('performed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('available_quantity', models.IntegerField(default=0)),
                ('reorder_point', models.IntegerField(default=0)),
                ('barcode', models.CharField(blank=True, max_length=100, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('unit_of_measurement', models.CharField(choices=[('pcs', 'pcs'), ('kg', 'kg'), ('liters', 'liters')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=100)),
                ('carrier_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VendorPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_time_delivery_rate', models.FloatField()),
                ('defect_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StockRecall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('success', models.BooleanField(default=False)),
                ('recalled_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_id', models.CharField(max_length=64)),
                ('location_id', models.CharField(max_length=64)),
                ('stock_level', models.IntegerField(default=0)),
                ('reserved_quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItemVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(max_length=64)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem')),
            ],
            options={
                'unique_together': {('product', 'vendor_id')},
            },
        ),
        migrations.CreateModel(
            name='InventorySerialNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem')),
            ],
            options={
                'unique_together': {('product', 'serial_number')},
            },
        ),
    ]
