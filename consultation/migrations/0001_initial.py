# Generated by Django 5.0.7 on 2024-07-26 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('joining_date', models.DateField()),
                ('phone', models.CharField(default='1234', max_length=12)),
                ('email', models.CharField(blank=True, default='exapmple@gmail.com', max_length=40)),
                ('department', models.ForeignKey(default='medicine', on_delete=django.db.models.deletion.CASCADE, to='consultation.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Patient/Photo')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], default='Prefer Not to say', max_length=1)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('occupation', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=1000, null=True, unique=True)),
                ('phone', models.CharField(blank=True, default='+91 12345678910', max_length=14, null=True)),
                ('email', models.CharField(blank=True, default='exapmple@gmail.com', max_length=40)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultation.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True, default='', null=True)),
                ('message', models.TextField(default='', max_length=1000)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultation.department')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultation.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.patient')),
            ],
        ),
    ]
