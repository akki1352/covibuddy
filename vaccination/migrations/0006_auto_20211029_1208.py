# Generated by Django 3.2.7 on 2021-10-29 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0005_auto_20211029_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='lname',
        ),
    ]
