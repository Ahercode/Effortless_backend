import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ahercode', '0028_remove_journals_posted_alter_transactions_bach_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalheaders',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='party',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='subscribers',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='bach_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ahercode.account')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ahercode.subscribers')),
            ],
            options={
                'db_table': 'Ahercode_account_details',
            },
        ),
    ]
