# Generated by Django 5.0.6 on 2024-08-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0003_alter_doctor_availability_alter_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
