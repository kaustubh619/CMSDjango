# Generated by Django 2.2.4 on 2019-12-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customCMS', '0002_auto_20191226_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesCMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('background_image', models.ImageField(upload_to='category_images')),
            ],
        ),
    ]
