# Generated by Django 5.0.6 on 2024-08-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
