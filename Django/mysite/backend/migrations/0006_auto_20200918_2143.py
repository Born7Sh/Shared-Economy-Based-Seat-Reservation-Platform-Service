# Generated by Django 3.1 on 2020-09-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_inquiry_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='tag1',
            field=models.CharField(default='hi', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cafe',
            name='tag2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
