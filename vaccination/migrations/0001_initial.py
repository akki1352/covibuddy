# Generated by Django 3.2.7 on 2021-10-25 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulances',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('fare', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CovidCentres',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=30)),
                ('availability', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('bedType', models.CharField(max_length=30)),
                ('availability', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('testType', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('location', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('supplyType', models.CharField(max_length=30)),
                ('stock', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=13)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('vaccineCost', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('duration', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]
