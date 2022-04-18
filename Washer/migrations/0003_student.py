# Generated by Django 4.0.4 on 2022-04-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Washer', '0002_washingmachine_occupied_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.PositiveSmallIntegerField()),
                ('wing', models.PositiveSmallIntegerField()),
                ('time_alloted', models.TimeField(default=None)),
                ('m_floor', models.PositiveSmallIntegerField()),
                ('m_wing', models.PositiveSmallIntegerField()),
                ('idntn', models.PositiveIntegerField()),
            ],
        ),
    ]
