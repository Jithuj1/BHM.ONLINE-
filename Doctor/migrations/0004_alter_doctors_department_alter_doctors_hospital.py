# Generated by Django 4.0.6 on 2023-01-10 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
        ('Doctor', '0003_doctors_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='Doctor.departments'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='working', to='Hospital.hospitals'),
        ),
    ]
