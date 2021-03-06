# Generated by Django 3.0.4 on 2020-03-28 18:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200327_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True, help_text='Creation date & time.')),
                ('content', models.TextField()),
            ],
        ),
    ]
