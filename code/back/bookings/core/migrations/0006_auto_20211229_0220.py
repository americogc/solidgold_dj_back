# Generated by Django 3.2.9 on 2021-12-29 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211227_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.date(2021, 12, 29)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.date(2021, 12, 30)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='hour_arrive',
            field=models.CharField(choices=[(0, '12:00 a. m.'), (1, '1:00 a. m.'), (2, '2:00 a. m.'), (3, '3:00 a. m.'), (4, '4:00 a. m.'), (5, '5:00 a. m.'), (6, '6:00 a. m.'), (7, '7:00 a. m.'), (8, '8:00 a. m.'), (9, '9:00 a. m.'), (10, '10:00 a. m.'), (11, '11:00 a. m.'), (12, '12:00 p. m.'), (13, '1:00 p. m.'), (14, '2:00 p. m.'), (15, '3:00 p. m.'), (16, '4:00 p. m.'), (17, '5:00 p. m.'), (18, '6:00 p. m.'), (19, '7:00 p. m.'), (20, '8:00 p. m.'), (21, '9:00 p. m.'), (22, '10:00 p. m.'), (23, '11:00 p. m.')], default=1, max_length=20),
        ),
    ]
