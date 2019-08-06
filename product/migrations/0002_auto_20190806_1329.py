# Generated by Django 2.2.4 on 2019-08-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.AlterField(
            model_name='product',
            name='dress_type',
            field=models.CharField(choices=[('shirt', 'Shirt'), ('t-shirt', 'T-Shirt'), ('pants', 'Pants'), ('trousers', 'Tro, blank = False, null = Falseusers')], max_length=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('vl', 'VL'), ('xl', 'XL'), ('26', 26), ('27', 27), ('28', 28), ('29', 29), ('30', 30), ('31', 31), ('32', 32), ('33', 33), ('34', 34), ('35', 35), ('36', 36), ('37', 37), ('38', 38), ('39', 39), ('40', 40), ('41', 41), ('42', 42)], max_length=3),
        ),
    ]
