# Generated by Django 4.2 on 2023-05-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafe', '0007_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/product.jpg', upload_to='products/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
