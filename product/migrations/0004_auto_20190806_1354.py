# Generated by Django 2.2.4 on 2019-08-06 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190806_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
