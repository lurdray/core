# Generated by Django 3.1.4 on 2021-01-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salebill',
            name='email',
            field=models.CharField(max_length=254),
        ),
    ]
