# Generated by Django 3.0.7 on 2021-04-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_user_sr_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='sr_number',
            field=models.IntegerField(),
        ),
    ]