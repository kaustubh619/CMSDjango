# Generated by Django 2.2.4 on 2019-12-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customCMS', '0005_auto_20191226_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycms',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
    ]
