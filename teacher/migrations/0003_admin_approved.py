# Generated by Django 3.1.7 on 2021-04-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210322_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
