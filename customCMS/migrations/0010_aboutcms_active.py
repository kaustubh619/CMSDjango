# Generated by Django 2.2.7 on 2019-12-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customCMS', '0009_aboutcms'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcms',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
