# Generated by Django 4.2.19 on 2025-03-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ahercode', '0009_alter_journal_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaldetails',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
