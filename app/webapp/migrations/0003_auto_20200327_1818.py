# Generated by Django 3.0.4 on 2020-03-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200327_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='stop_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]