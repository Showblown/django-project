# Generated by Django 4.2.1 on 2023-10-20 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_blood_sugar_healthdetails_blood_pressure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('years_of_experience', models.IntegerField()),
                ('specialization', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
            ],
        ),
    ]
