# Generated by Django 4.2 on 2023-04-21 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kafe', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created', 'name'), 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
    ]