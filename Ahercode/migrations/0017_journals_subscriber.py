# Generated by Django 4.2.19 on 2025-03-26 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ahercode', '0016_rename_journaldetails_journals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journals',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ahercode.subscribers'),
        ),
    ]
