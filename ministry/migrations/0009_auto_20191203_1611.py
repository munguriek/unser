# Generated by Django 2.2.6 on 2019-12-03 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0008_auto_20191203_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocateresource',
            name='amount_allocated',
        ),
        migrations.RemoveField(
            model_name='allocateresource',
            name='quantity_allocated',
        ),
    ]
