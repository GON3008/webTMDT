# Generated by Django 4.1.7 on 2023-04-10 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_new'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Oder_item',
            new_name='Order_item',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_oder',
            new_name='date_order',
        ),
        migrations.RenameField(
            model_name='order_item',
            old_name='oder',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='oder',
            new_name='order',
        ),
    ]
