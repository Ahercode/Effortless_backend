# Generated by Django 4.2.19 on 2025-03-26 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ahercode', '0018_alter_journals_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='journals',
            name='transaction_date',
            field=models.DateField(default=datetime.date(2025, 3, 26)),
        ),
    ]
