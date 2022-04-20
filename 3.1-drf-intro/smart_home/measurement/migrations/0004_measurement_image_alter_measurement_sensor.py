# Generated by Django 4.0.3 on 2022-04-20 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
