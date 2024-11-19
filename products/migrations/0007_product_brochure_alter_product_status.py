# Generated by Django 5.1.3 on 2024-11-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brochure',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Brochure PDF'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, null=True, verbose_name='Availability'),
        ),
    ]