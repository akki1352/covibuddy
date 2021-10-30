# Generated by Django 3.2.7 on 2021-10-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0004_rename_type_covidtestinglabs_testtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covidcarecentres',
            old_name='cost',
            new_name='availability',
        ),
        migrations.RenameField(
            model_name='covidcarecentres',
            old_name='testType',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='covidtestinglabs',
            name='availability',
        ),
        migrations.AddField(
            model_name='covidtestinglabs',
            name='cost',
            field=models.CharField(default=int, max_length=30),
            preserve_default=False,
        ),
    ]
