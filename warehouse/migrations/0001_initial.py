# Generated by Django 4.2.3 on 2023-07-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=16, verbose_name='Order number')),
                ('status', models.CharField(choices=[('New', 'New'), ('In Process', 'In Process'), ('Stored', 'Stored'), ('Send', 'Send')], default='New', max_length=16, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Warehouse order',
                'verbose_name_plural': 'Warehouse orders',
                'ordering': ('status',),
            },
        ),
    ]
