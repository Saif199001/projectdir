# Generated by Django 5.0.6 on 2024-07-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='mobileno',
            field=models.IntegerField(),
        ),
    ]
