# Generated by Django 3.1 on 2020-10-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTeam', '0002_auto_20201016_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='img_profile',
            field=models.FileField(blank=True, upload_to='media/images'),
        ),
    ]
