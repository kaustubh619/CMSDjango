# Generated by Django 2.2.7 on 2020-01-28 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0007_auto_20200127_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='productratingsandreviews',
            name='added_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]