# Generated by Django 3.1 on 2020-10-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_age_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='check',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='age',
            name='age10',
            field=models.IntegerField(default=0, verbose_name='age10'),
        ),
        migrations.AlterField(
            model_name='age',
            name='age20',
            field=models.IntegerField(default=0, verbose_name='age20'),
        ),
        migrations.AlterField(
            model_name='age',
            name='age30',
            field=models.IntegerField(default=0, verbose_name='age30'),
        ),
        migrations.AlterField(
            model_name='age',
            name='age40',
            field=models.IntegerField(default=0, verbose_name='age40'),
        ),
        migrations.AlterField(
            model_name='age',
            name='age50',
            field=models.IntegerField(default=0, verbose_name='age50'),
        ),
        migrations.AlterField(
            model_name='age',
            name='over60',
            field=models.IntegerField(default=0, verbose_name='over60'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='man',
            field=models.IntegerField(default=0, verbose_name='man'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='woman',
            field=models.IntegerField(default=0, verbose_name='woman'),
        ),
    ]
