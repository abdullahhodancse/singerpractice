# Generated by Django 5.0.6 on 2024-07-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=11)),
                ('instrument', models.CharField(max_length=110)),
            ],
        ),
    ]
