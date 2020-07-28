# Generated by Django 3.0.8 on 2020-07-28 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200728_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='StartDiagnosis',
            field=models.DateField(default=datetime.date(2020, 7, 29), null=True),
        ),
        migrations.AlterField(
            model_name='epicrisis',
            name='HospitalDischarge',
            field=models.DateField(default=datetime.date(2020, 7, 29), null=True),
        ),
        migrations.AlterField(
            model_name='epicrisis',
            name='Hospitalization',
            field=models.DateField(default=datetime.date(2020, 7, 29), null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='DateForm',
            field=models.DateField(default=datetime.date(2020, 7, 29)),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='Date',
            field=models.DateField(default=datetime.date(2020, 7, 29)),
        ),
    ]
