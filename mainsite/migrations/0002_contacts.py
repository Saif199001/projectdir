# Generated by Django 5.0.6 on 2024-07-15 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=20)),
                ('studentemail', models.EmailField(max_length=254)),
                ('coursename', models.CharField(max_length=50)),
                ('mobileno', models.IntegerField(max_length=10)),
                ('massage', models.TextField(max_length=100)),
            ],
        ),
    ]
