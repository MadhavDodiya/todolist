# Generated by Django 5.0.6 on 2024-07-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
