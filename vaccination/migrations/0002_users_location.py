# Generated by Django 3.2.7 on 2021-10-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='location',
            field=models.CharField(default=str, max_length=30),
            preserve_default=False,
        ),
    ]
