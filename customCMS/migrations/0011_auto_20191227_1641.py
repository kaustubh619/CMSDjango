# Generated by Django 2.2.7 on 2019-12-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customCMS', '0010_aboutcms_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcms',
            name='about_image',
            field=models.ImageField(blank=True, null=True, upload_to='about_images'),
        ),
    ]
